"""
Ready for Level 3? (The Real-World Log Parser)
Since you crushed the cipher challenges, let's look at how slicing is used in the real world: parsing raw data streams.

Challenge #3: "Extract the Timestamp"
Imagine you are pulling data from a server log, but the format is messy. You receive this string:

Python
log_entry = "ERROR [2026-10-14T14:32:05Z] - Service timeout on port 8080"
Your Goal
Write a single line of Python code using only string slicing to extract just the date and time portion inside the brackets:
2026-10-14T14:32:05Z

Rule: Do not use .split(), .replace(), or find methods. Find the exact start and stop indices using positive or negative slicing!
"""

log_entry = "ERROR [2026-10-14T14:32:05Z] - Service timeout on port 8080"
timestamp = log_entry[7:27]
print(timestamp)
