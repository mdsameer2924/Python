def greet(name: str, msg: str) -> None:
    print(f"Hello {name},\nI've message for you: {msg}")


name: str = input("Enter your Name: ")
usrname = name or "guest"
greet(usrname, "shaadi mein jana hain dost ki")
age: int
