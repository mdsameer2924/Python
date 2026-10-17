# method overriding (we need inheritance)
class Animal:
    def __init__(self, name):
        self.name = name

    ## Method overriding
    def details(self):
        print(f"Animal Name is {self.name}")


class Human(Animal):
    def __init__(self, name):
        super().__init__(name)

    ## method overidden
    def details(self):
        print(f"Human Name is {self.name}")


h = Human("Sameer")
h.details()

""" 
Method overloading does not support in python
we can achieve similar behaviour using *args
"""
