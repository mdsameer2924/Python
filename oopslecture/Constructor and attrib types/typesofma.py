## file name: types of method and attributes
from re import purge


class Animal:
    x = 30  # class attributes

    # Constructor
    def __init__(self, name):
        self.name = name  # object/instance attributes

    def hello(self):  # object/instance methods
        print("Hlo how are you")

    @classmethod
    def check(cls):
        print("hi i am asking class  attributes here ", cls.x)

    @staticmethod
    def display_salam():
        print("Asalamualaikum!")


dog = Animal("Sheru")
dog.check()  ## accessing class's methods
Animal.display_salam()
