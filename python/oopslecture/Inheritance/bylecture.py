class Animal:
    def __init__(self, name):
        self.name = name


class Human:
    def __init__(self, id):
        self.id = id


class Robot(Animal, Human):
    def __init__(self, name, id):
        Animal.__init__(self, name)
        Human.__init__(self, id)


p = Robot("sameer", 34)
print(p.id)
