class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"my name is {self.name}"


class Numbers:
    def __init__(self, num) -> None:
        self.num = num

    def __add__(self, other) -> int:
        return self.num + other.num

    def __str__(self) -> str:
        return f"number is: {self.num}"


obj = Animal("lion")

print(obj)

nobj = Numbers(4)
mobj = Numbers(5)
print(nobj + mobj)
