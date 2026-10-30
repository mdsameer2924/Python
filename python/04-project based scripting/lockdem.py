#!/usr/bin/python3

## Use gocryptfs automatic password changer and store new password into keyde

## Module Import
from pathlib import Path
import subprocess
import sys
import pexpect  # third party module
import argparse
import color as log

# -------------------------------------------------------------------------
## Path configuration
pass_script = Path.home() / "bin" / "pass"
secfile = Path.home() / "Documents" / "secure.file"
cipher_dir = secfile / "VzA"
newp = secfile / "newpass"
oldp = secfile / "recentpass"
# -------------------------------------------------------------------------

# flag generated
parse = argparse.ArgumentParser(
    usage="%(prog)s [options]",
    description="Bootstrap script and to automate encryption task",
)
parse.add_argument("-c", "--change", action="store_true", help="to change password")
get_parse = parse.parse_args()

if get_parse.change:
    # genrate new password
    try:
        with open(newp, "w") as fc:
            subprocess.run(
                [pass_script, "16"],
                check=True,
                stdout=fc,
                stderr=subprocess.DEVNULL,
                encoding="utf-8",
                timeout=10,
            )
    except subprocess.CalledProcessError:
        log.log_err("something is wrong review source code password genrating part")
        sys.exit(1)

    except subprocess.TimeoutExpired:
        log.log_err("Time excceed for generating password")
        sys.exit(1)
    except Exception as e:
        log.log_err(f"An Unexpected error occur: {e}")
        sys.exit(1)

    else:
        log.log_ok(f"new password generated in {newp.name} file")

    # Read password
    try:
        with open(newp, "r") as np:
            new_pass = np.read().strip()

        with open(oldp, "r") as op:
            old_pass = op.read().strip()
    except Exception as e:
        log.log_err(f"An Unexpected error to read password: {e}")
        sys.exit(1)

    ### Change password using gocryptfs
    try:
        child = pexpect.spawn(f"gocryptfs -passwd {cipher_dir}", encoding="utf-8")
        child.expect("Password:")
        child.sendline(old_pass)

        child.expect("Please enter your new password.")
        child.expect("Password:")
        child.sendline(new_pass)

        child.expect("Repeat:")
        child.sendline(new_pass)
        child.interact()
        try:
            subprocess.run(["cp", newp, oldp], check=True, timeout=3)
        except subprocess.CalledProcessError:
            log.log_err("old password not update")
            sys.exit(0)

    except KeyboardInterrupt:
        log.log_warn(f"You Cancel program forcefully")
    except Exception as e:
        log.log_err(f"Unexpected Error {e}")
        sys.exit(1)
    else:
        log.log_ok(f"password successfuly changed!")

    try:
        log.log_info(f"new password: {new_pass}")
        choose = input("Would you like to copy new password directly [y/n]: ")
        if choose == "y":
            subprocess.run(["clip-c", newp], check=True, timeout=5)

    except (subprocess.CalledProcessError, os.error):
        log.log_err(f"Error occur review source code")
        sys.exit(1)
    except subprocess.TimeoutExpired:
        log.log_err("Unexpected error: TimeOut")
        sys.exit(1)
else:
    print("use -h for help to use it")
    print(f"example:- ./{sys.argv[0]} -h")
