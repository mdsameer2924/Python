choice = int(input("Enter your choice: "))
name = input("Enter your name: ")
if choice == 1:
    if name.isupper():
        print("word is upper")
        print("x".upper() in name)  # in is an membership opeartor  recent
    else:
        print("word is not upper")
elif choice == 2:
    if name.islower():
        print("word is lower")
    else:
        print("word is not lower")
elif choice == 3:
    if name.istitle():
        print("word is capitalized")
    else:
        print("word is not capitalized")
else:
    print("invalid Choice")
