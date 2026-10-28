def dec(func):
    def wrapper():
        print("HI")
        func()
        print("BYe")
        return wrapper()


@dec
def hello():
    print("Sameer")


hello()
