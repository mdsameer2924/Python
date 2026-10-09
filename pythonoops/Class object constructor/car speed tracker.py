# Car Speed Tracker
# Construct a class named Car that accepts brand and speed (in km/h) in its constructor. 
# Write a method accelerate(increase) that increases the car's speed by the given amount, and a method brake(decrease) that reduces it 
# (ensure the speed never drops below 0).

class Car:
    def __init__(self,brand,speed=0.0):
        self.brand=brand
        self.speed=speed
    def accelerate(self,increase):
            self.speed+=increase
            return f"speed increased by {increase}km/h\nCurrent speed is {self.speed}km/h"
    def brake(self,decrease):
                self.speed-=decrease
                if self.speed>=0:
                    return f"speed decreased by {decrease}km/h\nCurrent speed is {self.speed}km/h"
                else:
                    self.speed=0
                    return f"speed decreased by {decrease}km/h\nCurrent speed is {self.speed}km/h"
                    


hv=Car('toyato',50)
print(hv.accelerate(4))
print(hv.brake(79))