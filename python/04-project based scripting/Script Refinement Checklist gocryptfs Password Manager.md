# Script Refinement Checklist: gocryptfs Password Manager

*A learn-by-doing guide for polishing Script 1 by hand, with hints but no finished code.*

Building Script 1 yourself through the write, get stuck, learn, break loop is a strong way to learn, and the fact that it works and solves your own problem counts for more than which script is "better". Work through the sections below in order.

## 1. Correctness first (the lockout bug)

This is the only issue that can actually hurt you, so fix it before anything else.

- **Concept:** a process's *exit status*. Learn what `child.expect(pexpect.EOF)`, `child.close()` and `child.exitstatus` do.
- **Rule:** never overwrite `recentpass` until you know gocryptfs succeeded. Order of operations matters.
- **Bonus concept, atomic writes:** write to a temp file, then use `os.replace(tmp, final)`. The file is then either fully old or fully new, never half-written.

## 2. Structure

- Wrap the logic in functions that each do one thing (`generate_password()`, `change_gocryptfs_password()`, `lock_file()`, and so on), plus a `main()`.
- End the file with `if __name__ == "__main__":` and call `main()` there. Learn why this matters: right now everything runs the moment the file is imported.
- Functions should **return values or raise exceptions**. Only `main()` should call `sys.exit()` and print errors. Calling `sys.exit` deep inside helpers makes code hard to reuse and test.
- Delete dead code, like the unused decorator and the empty stubs, once the real functions exist.

## 3. Dependency handling

Auto-running `sudo apt install` at import time is the thing professionals avoid most. The standard approach is to check whether the tool exists with `shutil.which`, print a clear message ("gocryptfs not found, install it with ..."), and exit. Document requirements in a README. Your future self will thank you.

## 4. argparse

- Learn `add_mutually_exclusive_group()` so `-c -t` can't be combined.
- Learn **subcommands** (`add_subparsers`), which give you `script change`, `script lock <time>`, `script unlock`, `script watch`. This is how `git` and `docker` work, and it suits your script well.
- If `--timelock` needs a time, validate it with `parser.error(...)` instead of catching `TypeError` later.

## 5. Security

- Set `os.umask(0o077)` or `os.chmod(path, 0o600)` so password files are owner-only.
- Use `pexpect.spawn("gocryptfs", ["-passwd", str(cipher_dir)])` with an argument list instead of an f-string command. It avoids shell and quoting problems with paths.
- Learn why `subprocess` takes lists and why you never build shell strings from variables.
- Think about what happens to the plaintext password after you copy it to the clipboard, and whether it should be cleared after some seconds.

## 6. Error handling

- Replace broad `except Exception` with specific ones: `FileNotFoundError`, `PermissionError`, `subprocess.CalledProcessError`, `subprocess.TimeoutExpired`.
- Learn `try / except / else / finally` properly. Your use of `else` is already good.
- Every `subprocess.run` that can fail should have a `timeout` and a specific handler.

## 7. Code style (the "industry standard" part)

- Read **PEP 8** and learn the naming rules: constants like `PASS_SCRIPT` in uppercase, and descriptive names instead of `np`, `op`, `fc`. (`np` also collides with the universal numpy alias.)
- Add **type hints** (`def lock_file(path: Path, when: str) -> None:`) and short **docstrings**.
- Install **ruff** (linter and formatter in one tool) and run `ruff check` and `ruff format`. It will teach you style rules automatically.
- Later, try **mypy** to see what type hints catch.
- Fix spelling in messages, such as "genrated" and "excceed".

## 8. Logging

Your `color` module works. The next step is Python's built-in `logging` module with levels (INFO, WARNING, ERROR). It is worth learning even if you keep your colors on top.

## 9. Habits that make you professional

- Put the project in **git** and commit after each refactor step so you can undo mistakes.
- Write a short README with usage and requirements.
- Once you're comfortable, learn **pytest** and `unittest.mock` to test functions without touching your real encrypted data. Test against a throwaway gocryptfs directory, never your real `Zin`.

## Suggested order

1. Fix the exit-status and ordering bug.
2. Split into functions and add `main()`.
3. Switch to subcommands or a mutually exclusive group.
4. Handle dependencies and permissions.
5. Run ruff, add type hints, then do the naming cleanup.
6. Commit to git and write the README.

## Before you change anything

**Back up your gocryptfs config** (`gocryptfs.conf` in `Zin`). It holds the encrypted master key, and a bad password change is the one way this project can lose data.

When you've done a step or two, review your version and look for what to improve without rewriting it wholesale.
