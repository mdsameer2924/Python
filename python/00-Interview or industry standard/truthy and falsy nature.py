"""
in python each and every object contain it's nature in boolean means either False or True
understanding this nature helps to standout in interview and master coding in a pythonic style
for example!
"""

name = input("Enter your name: ")
if name:
    print("Truthy if string got even one letter")  # eg "l" == Truthy
else:
    print("falsy if user just press enter without giving input")  # "" == falsy

username = name or "guest"
print(f"logged in as {username}")
