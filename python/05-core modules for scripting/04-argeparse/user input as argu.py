import argparse
import sys
from pathlib import Path

par = argparse.ArgumentParser(
    usage="%(prog)s [option] [path]", description="File Handling Toolkit"
)

# Your existing flag
par.add_argument(
    "-ch", "--check", action="store_true", help="to check existence of a file"
)

# NEW: Add a positional argument for the path.
# nargs="?" makes it optional so the script doesn't crash if they forget to type a path.
# default="." means it falls back to the current directory if no path is given.
par.add_argument("target_path", nargs="?", default=".", help="Path to check")

flg = par.parse_args()

# Convert the string path into a pathlib Path object
path_to_check = Path(flg.target_path)

if flg.check:
    if path_to_check.exists():
        print(f"Path exists: {path_to_check.resolve()}")
        sys.exit(0)
    else:
        print(f"Path does not exist: {path_to_check.resolve()}")
        sys.exit(1)
