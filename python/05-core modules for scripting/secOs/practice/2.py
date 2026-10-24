import os
import log as show

show.log_info(
    "Check for the DB_PASSWORD environment variable using os.getenv(), printing a fallback message if it doesn't exist."
)
"""
ch = os.getenv("DB_PASSWORD", "")
if ch == "":
    show.log_err(f"{ch} doesn't exist")
else:
    print(ch)
"""

db_password = os.getenv("DB_PASSWORD")
print(db_password)
if db_password == None:
    show.log_err("printing a fallback message if it doesn't exist.")
    db_password = "dfcieg_43"
else:
    show.log_ok("DB is Found")
    print(db_password)
