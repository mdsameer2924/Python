def dec(func):
    def wrapper():
        print("HI")
        func()
        print("BYe")

    return wrapper


@dec
def hello():
    print("Sameer")


@dec
def add() -> None:
    a: int = 3
    b: int = 6
    print(a + b)


hello()
print("\n")
add()
