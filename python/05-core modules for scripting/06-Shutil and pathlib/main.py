#!/usr/bin/python3

import time
import shutil
from pathlib import Path
import subprocess
import log
import argparse

# -------------------------------------------------------------
parse = argparse.ArgumentParser(description="File manipulation CLI- tool")
parse.add_argument(
    "-f", "--filecheck", action="store_true", help="to check path is file or directory"
)
parse.add_argument("-wr", action="store_true", help="to import output into txt file")
ps = parse.parse_args()


bas_dir = Path.home() / "Desktop"
syb = bas_dir / "Javaoops"
# for list in bas_dir.iterdir():
#     print(list)

if ps.filecheck:
    if syb.is_file():
        print(f"{syb.name} is file")
    else:
        print(f"{syb.name} is directory")
## file handling to dumpt it's output into a new genrated file
elif ps.wr:
    try:
        with open("new.txt", "w") as cr:
            subprocess.run(
                ["ls", syb], encoding="utf-8", stdout=cr, check=True, timeout=0.01
            )

        subprocess.run(
            ["ls", "--color=always", syb], encoding="utf-8", check=True, timeout=1
        )
        log.log_info("Txt file is creating wait...")
    except subprocess.CalledProcessError:
        log.log_err("something went wrong check source code")

    except subprocess.TimeoutExpired:
        log.log_err("Something stuck or freeze Time out Error!.")
    else:
        time.sleep(3)
        log.log_ok("output successfully redirected into new.txt")
