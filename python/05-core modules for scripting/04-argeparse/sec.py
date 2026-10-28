import argparse
import sys
from pathlib import Path

par = argparse.ArgumentParser(
    usage="%(prog)s [option] [path]", description="File Handling Toolkit"
)

par.add_argument(
    "-ch", "-check", action="store_true", help="to check existance of a file"
)

flg = par.parse_args()

if flg.ch:
    print("path exist")
