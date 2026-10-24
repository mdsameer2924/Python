#!/usr/bin/python3
# try:
#     a = int(input("enter number"))
# except ValueError:
#     print(f"Your input is string {a}!")
#     print("Try again! give input as number")
# else:
#     print(a)

giving = True
while giving:
    user_input = input("Enter number: ")
    try:
        a = float(user_input)
    except ValueError:
        print(f"'{user_input}' is not a valid number. Try again!\n")
    else:
        print(f"Success! You entered: {a}")
        break
