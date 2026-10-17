"""
Practice Question 2: Designing with Mixins and Cooperative Inheritance
You are building a game character system. You need to create a SuperHero class using multiple inheritance and cooperative super() calls.

Requirements:
Create a base class Character that takes a name in its __init__ and stores it.

Create a mixin class Flyer that adds a fly() method printing "{name} is soaring through the sky!" and uses super() correctly.

Create a mixin class Invisibler that adds a hide() method printing "{name} has vanished!" and uses super() correctly.

Create a final class SuperHero that inherits from Character, Flyer, and Invisibler (in that order).
Your Tasks:
Write the code for all four classes ensuring that cooperative multiple inheritance (super()) is used correctly in every __init__ so that argument passing does not break.

Instantiate obj = SuperHero(name="Vortex") and verify that calling obj.fly() and obj.hide() works seamlessly.
"""


class Character:
    def __init__(self, name):
        self.name = name


class Flyer(Character):
    def __init__(self, name):
        super().__init__(name)

    # method
    def fly(self):
        print(f"{self.name} is soaring through the sky!.")


class Invisibler(Character):
    def __init__(self, name):
        super().__init__(name)

    # method
    def hide(self):
        print(f"{self.name} has vanished!.")


class SuperHero(Character, Flyer, Invisibler):
    def __init__(self, name):
        Character.__init__(self, name)
        Flyer.__init__(self, name)
        Invisibler.__init__(self, name)


obj = SuperHero("Monkey d luffy")
obj.fly()
obj.hide()
