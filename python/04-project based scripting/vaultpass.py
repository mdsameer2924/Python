#!/usr/bin/env python3
"""vaultpass - manage the gocryptfs password for the Zin vault.

Commands:
    change   generate a new password and apply it to the gocryptfs vault
    lock     time-lock the stored password with tlescr
    unlock   decrypt the time-locked password
    watch    show the countdown until the lock opens

Reference rewrite written to demonstrate common sysadmin/DevOps practices.
Lines tagged "PRACTICE" explain *why* something is done the way it is.
"""

# PRACTICE: `from __future__ import annotations` lets type hints use modern
# syntax (`int | None`) and avoids evaluating them at import time.
from __future__ import annotations

import argparse
import logging
import os
import shutil
import subprocess
import sys
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

# PRACTICE: imports in three groups (stdlib, third party, local), separated
# by blank lines. Third-party packages are declared in a README/requirements
# file, never installed by the script itself.
import pexpect

LOG = logging.getLogger("vaultpass")

# PRACTICE: magic numbers become named constants (UPPER_CASE) at the top.
PASSWORD_LENGTH = 16
GENERATE_TIMEOUT = 10
GOCRYPTFS_TIMEOUT = 30
TLESCR_TIMEOUT = 20
TLESCR_DECRYPT_TIMEOUT = 40
CLIPBOARD_TIMEOUT = 5


# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Config:
    """All paths in one place. Frozen = cannot be changed by accident."""

    pass_script: Path
    cipher_dir: Path
    current_pass: Path
    locked_pass: Path
    backup_dir: Path

    @classmethod
    def default(cls) -> Config:
        secure = Path.home() / "Documents" / "secure.file"
        return cls(
            pass_script=Path.home() / "bin" / "pass",
            cipher_dir=secure / "Zin",
            current_pass=secure / "recentpass",
            locked_pass=secure / "recentpass.enc",
            backup_dir=secure,
        )

    @property
    def pending_pass(self) -> Path:
        return self.current_pass.with_name(self.current_pass.name + ".pending")


# --------------------------------------------------------------------------
# Errors
# --------------------------------------------------------------------------
class VaultError(Exception):
    """An expected failure with a message that is safe to show the user.

    PRACTICE: helpers raise exceptions; only main() decides how to report
    them and which exit code to use. Helpers never call sys.exit().
    """


# --------------------------------------------------------------------------
# Generic helpers (reusable in any future script)
# --------------------------------------------------------------------------
def setup_logging(verbose: bool) -> None:
    """Send log output to stderr, keeping stdout clean for real output."""
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )


def require_tool(name: str) -> None:
    """Fail early with a clear message instead of installing things silently."""
    if shutil.which(name) is None:
        raise VaultError(f"required tool not found in PATH: {name}")


def run(
    cmd: list[str],
    *,
    timeout: int | None,
    capture: bool = False,
) -> subprocess.CompletedProcess[str]:
    """Run a command with a list of args (never a shell string).

    PRACTICE: one wrapper translates low-level subprocess errors into one
    error type, so callers do not repeat the same try/except blocks.
    """
    LOG.debug("running: %s", cmd)
    try:
        return subprocess.run(
            cmd,
            check=True,
            timeout=timeout,
            text=True,
            capture_output=capture,
        )
    except FileNotFoundError as exc:
        raise VaultError(f"command not found: {cmd[0]}") from exc
    except subprocess.TimeoutExpired as exc:
        raise VaultError(f"{cmd[0]} timed out after {timeout}s") from exc
    except subprocess.CalledProcessError as exc:
        raise VaultError(f"{cmd[0]} failed with exit code {exc.returncode}") from exc


def read_secret(path: Path) -> str:
    try:
        return path.read_text().strip()
    except OSError as exc:
        raise VaultError(f"cannot read {path}: {exc.strerror}") from exc


def write_secret(path: Path, content: str) -> None:
    """Write a secret so the file is never world-readable or half-written.

    PRACTICE: create with mode 0600 from the start (no window where it is
    readable), write to a temp file, fsync, then os.replace() it into place.
    os.replace is atomic: readers see the old file or the new one, never a mix.
    """
    tmp = path.with_name(path.name + ".tmp")
    try:
        fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        os.fchmod(fd, 0o600)
        with os.fdopen(fd, "w") as handle:
            handle.write(content + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    except OSError as exc:
        tmp.unlink(missing_ok=True)
        raise VaultError(f"cannot write {path}: {exc.strerror}") from exc


def copy_to_clipboard(path: Path) -> None:
    require_tool("clip-c")
    run(["clip-c", str(path)], timeout=CLIPBOARD_TIMEOUT)
    LOG.info("copied to clipboard")


# --------------------------------------------------------------------------
# Feature logic (each function does exactly one job)
# --------------------------------------------------------------------------
def generate_password(cfg: Config) -> str:
    """Generate a password in memory; it never touches the disk here."""
    if not os.access(cfg.pass_script, os.X_OK):
        raise VaultError(f"password generator not executable: {cfg.pass_script}")
    result = run(
        [str(cfg.pass_script), str(PASSWORD_LENGTH)],
        timeout=GENERATE_TIMEOUT,
        capture=True,
    )
    password = result.stdout.strip()
    if not password:
        raise VaultError("password generator returned nothing")
    return password


def backup_gocryptfs_conf(cfg: Config) -> Path:
    """Copy gocryptfs.conf (holds the encrypted master key) before changing it."""
    conf = cfg.cipher_dir / "gocryptfs.conf"
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = cfg.backup_dir / f"gocryptfs.conf.{stamp}.bak"
    try:
        shutil.copy2(conf, backup)
        backup.chmod(0o600)
    except OSError as exc:
        raise VaultError(f"cannot back up {conf}: {exc.strerror}") from exc
    return backup


def gocryptfs_change_password(cipher_dir: Path, old: str, new: str) -> None:
    """Drive `gocryptfs -passwd`. Returns only if gocryptfs reports success."""
    require_tool("gocryptfs")
    # PRACTICE: argument list, not an f-string command, so odd characters in
    # a path can never be misread as shell syntax.
    child = pexpect.spawn(
        "gocryptfs",
        ["-passwd", str(cipher_dir)],
        encoding="utf-8",
        timeout=GOCRYPTFS_TIMEOUT,
    )
    try:
        child.expect("Password:")
        child.sendline(old)
        child.expect("Please enter your new password.")
        child.expect("Password:")
        child.sendline(new)
        child.expect("Repeat:")
        child.sendline(new)
        child.expect(pexpect.EOF)
    except pexpect.TIMEOUT as exc:
        raise VaultError("gocryptfs timed out waiting for a prompt") from exc
    except pexpect.EOF as exc:
        raise VaultError(
            "gocryptfs exited early (wrong old password or bad vault path?)"
        ) from exc
    finally:
        child.close()  # PRACTICE: always release the child process.

    # PRACTICE: trust the exit status, not the absence of an exception.
    if child.exitstatus != 0:
        raise VaultError(f"gocryptfs failed (exit status {child.exitstatus})")


# --------------------------------------------------------------------------
# Command handlers: one per subcommand, all with the same signature
# --------------------------------------------------------------------------
def cmd_change(cfg: Config, args: argparse.Namespace) -> None:
    if cfg.pending_pass.exists():
        raise VaultError(
            f"leftover {cfg.pending_pass.name} found: a previous change may have "
            "been interrupted. Check it before continuing."
        )

    old = read_secret(cfg.current_pass)
    new = generate_password(cfg)
    LOG.info("new password generated")

    backup = backup_gocryptfs_conf(cfg)
    LOG.info("vault config backed up to %s", backup)

    # PRACTICE (write-ahead): save the new password BEFORE applying it, so a
    # crash mid-change can never leave you with a changed vault and no record
    # of the password.
    write_secret(cfg.pending_pass, new)
    try:
        gocryptfs_change_password(cfg.cipher_dir, old, new)
    except VaultError:
        cfg.pending_pass.unlink(missing_ok=True)  # vault unchanged, discard
        raise

    # Only now, after confirmed success, the new password becomes current.
    os.replace(cfg.pending_pass, cfg.current_pass)
    LOG.info("password changed successfully")

    if args.copy:
        copy_to_clipboard(cfg.current_pass)


def cmd_lock(cfg: Config, args: argparse.Namespace) -> None:
    require_tool("tlescr")
    if not cfg.current_pass.exists():
        raise VaultError(f"nothing to lock: {cfg.current_pass.name} does not exist")

    run(
        ["tlescr", "encrypt", str(cfg.current_pass), "--at", args.when],
        timeout=TLESCR_TIMEOUT,
    )

    # PRACTICE: verify the result before the destructive step. Deleting the
    # plaintext without confirming the .enc file exists could destroy the
    # only copy of the password.
    if not cfg.locked_pass.exists():
        raise VaultError(
            f"{cfg.locked_pass.name} was not created; plaintext kept for safety"
        )
    cfg.current_pass.unlink()
    LOG.info("%s locked until %s", cfg.current_pass.name, args.when)


def cmd_unlock(cfg: Config, args: argparse.Namespace) -> None:
    if cfg.current_pass.exists():
        LOG.warning("password is already unlocked")
    else:
        require_tool("tlescr")
        if not cfg.locked_pass.exists():
            raise VaultError(f"{cfg.locked_pass.name} not found: nothing to unlock")
        run(
            ["tlescr", "decrypt", str(cfg.locked_pass)],
            timeout=TLESCR_DECRYPT_TIMEOUT,
        )
        if not cfg.current_pass.exists():
            raise VaultError("decrypt finished but no password file appeared")
        cfg.locked_pass.unlink()
        LOG.info("password unlocked")

    if args.copy:
        copy_to_clipboard(cfg.current_pass)


def cmd_watch(cfg: Config, args: argparse.Namespace) -> None:
    require_tool("tlescr")
    if not cfg.locked_pass.exists():
        raise VaultError("password is not locked")
    try:
        run(["tlescr", "watch", str(cfg.locked_pass)], timeout=None)
    except KeyboardInterrupt:
        LOG.info("countdown cancelled")


# --------------------------------------------------------------------------
# Command line interface
# --------------------------------------------------------------------------
Handler = Callable[[Config, argparse.Namespace], None]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vaultpass",
        description="Manage and time-lock the gocryptfs vault password.",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="show debug output"
    )

    # PRACTICE: subcommands (like git/docker). Argparse validates required
    # arguments per command, and mutually exclusive actions are automatic.
    sub = parser.add_subparsers(dest="command", required=True, metavar="COMMAND")

    p_change = sub.add_parser("change", help="change the vault password")
    p_change.add_argument("--copy", action="store_true", help="copy new password")
    p_change.set_defaults(handler=cmd_change)

    p_lock = sub.add_parser("lock", help="time-lock the stored password")
    p_lock.add_argument(
        "when",
        help="unlock time: '2026-12-02 15:30:00' or a duration such as 2d, 3h, 30m",
    )
    p_lock.set_defaults(handler=cmd_lock)

    p_unlock = sub.add_parser("unlock", help="unlock the stored password")
    p_unlock.add_argument("--copy", action="store_true", help="copy password")
    p_unlock.set_defaults(handler=cmd_unlock)

    p_watch = sub.add_parser("watch", help="show time left on the lock")
    p_watch.set_defaults(handler=cmd_watch)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    setup_logging(args.verbose)
    os.umask(0o077)  # PRACTICE: every file we create is owner-only by default.

    if os.geteuid() == 0:
        LOG.warning("running as root: ~ now points to root's home directory")

    cfg = Config.default()
    handler: Handler = args.handler
    try:
        handler(cfg, args)
    except VaultError as exc:
        LOG.error("%s", exc)
        return 1
    except KeyboardInterrupt:
        LOG.warning("interrupted")
        return 130  # PRACTICE: 128 + SIGINT(2), the shell convention.
    return 0


# PRACTICE: importing this file (for tests) runs nothing; only executing it does.
if __name__ == "__main__":
    sys.exit(main())
