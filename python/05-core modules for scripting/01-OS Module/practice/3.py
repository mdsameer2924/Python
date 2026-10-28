import log as show
import os
import time

"""
Check if the app_logs directory exists in the current folder using os.path.exists().
If it doesn't exist, create it using os.mkdir().import
"""
dir_path = "./app_log/"
isdir = os.path.exists(dir_path)
if isdir:
    show.log_ok("Directory Exist!")
else:
    show.log_info("Directory is Creating...")
    os.mkdir(dir_path)
    time.sleep(1)
    show.log_ok("Directory has been created.")
