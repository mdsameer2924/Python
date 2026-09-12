class Dog:
    def make_sound(self):
        return "woof!"

class  Cat:
    def make_sound(self):
        return "meow!"

class Lion:
    def make_sound(self):
        return "roar"

def animal(object):
    print(object.make_sound()) 

a=Dog()
b=Cat()
c=Lion()
animal(a)
animal(b)
animal(c)