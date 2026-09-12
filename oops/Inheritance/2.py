# Create a parent class named Vehicle with an __init__ constructor that accepts brand and speed, and
# a method get_info() that returns a string formatted as "Brand: {self.brand}, Speed: {self.speed} km/h".

class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def get_info(self):
        return f"Brand: {self.brand}, Speed: {self.speed} km/h"

class ElectricCar(Vehicle):
    def __init__(self,brand,speed,battery_capacity):
        super().__init__(brand,speed)
        self.battery_capacity=battery_capacity

    def get_info(self):
        return f"{super().get_info()}, Battery_capacity: {self.battery_capacity} km/h "

suz=ElectricCar('toyato',40,150)
print(suz.get_info())