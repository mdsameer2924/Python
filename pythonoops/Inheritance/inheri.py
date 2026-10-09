class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f"{self.name} makes sound"
    def eat(self,food):
        return f"eating {food}"

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def speak(self):
        return f"{self.name} the {self.breed} barks: Woof!"

ga=Animal('creature')
print(ga.speak())
sd=Dog('jack','german sehpard')
print(sd.speak())
print(sd.eat('chocolate'))
