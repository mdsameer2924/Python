# create a class named Temperature that initializes with a private attribute __celsius (default to 0).
# write a getter method get_celsius() and a setter method set_celsius(value) that ensures the temperature is never set below -273.15°C (absolute zero). 
# If a lower value is passed, print an error message instead of updating the value.

class Temperature:
    def __init__(self,celsius=0):
        self.__celsius=celsius

    ## getter method to access private attributes
    def get_celsius(self):
        return f"Air conditioner temprature: {self.__celsius}°C"
    ## setter method to modify private attributes
    def set_celsius(self,val):
        if val< -273.15:    
            return f"error"
        self.__celsius=val
        return f"Air conditioner temprature setted to {self.__celsius}°C"
        
ac1=Temperature(39)
print(ac1.get_celsius())
ac1.set_celsius(49)
print(ac1.get_celsius())
print(ac1.set_celsius(58))
ac1.__celsius=42
print(ac1.get_celsius())
print(ac1.__celsius)