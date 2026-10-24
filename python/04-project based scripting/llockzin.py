#!/usr/bin/python3

import os
import subprocess

home = os.environ.get("USER", "")
print(home)
pat = os.path.join("idea", "hain", "mera", "pass")
print(pat)

command = subprocess.run(["tree", "."], capture_output=True, text=True, check=True)
print(command.stdout)

print("user uid", os.getuid())
