#!/usr/bin/python3
# import subprocess
#
# print("Do you want to update your system")
# print("\n")
# validating = True
# while validating:
#     choice = input("press [y/n]: ")
#     if choice == "y".lower():
#         runs = subprocess.run(
#             ["sudo", "apt", "update", "&&", "sudo", "apt", "upgrade"],
#             text=True,
#             capture_output=True,
#             check=True,
#         )
#         print(runs.stdout)
#         print("update succeed.")
#         break
#     elif choice == "n".lower():
#         print("you've cancel!")
#         print("exit..")
#         break
#     else:
#         print("invalid input. try again!")

import subprocess
import os
import sys

# Ensure the script is run with root privileges
if os.geteuid() != 0:
    print("[-] Error: This script must be run with sudo.")
    print("    Run it like this: sudo python3 script.py")
    sys.exit(1)

print("Do you want to update your system?")
choice = input("press [y/n]: ").strip().lower()

if choice == "y":
    try:
        print("\n[+] Updating package lists...")
        subprocess.run(["apt", "update"], check=True)

        print("\n[+] Upgrading packages...")
        # Added -y so apt doesn't stop and prompt for manual [Y/n] confirmation
        subprocess.run(["apt", "upgrade", "-y"], check=True)

        print("\n[OK] Update succeeded!")
    except subprocess.CalledProcessError as e:
        print(f"\n[ERROR] An error occurred during the update: {e}")
elif choice == "n":
    print("You've canceled!")
    print("Exit...")
else:
    print("Invalid input. Try again!")
