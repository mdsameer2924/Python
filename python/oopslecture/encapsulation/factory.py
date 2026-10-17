class Factory:
    __name = "maruti"  # Private class attributes

    def __init__(self, typee, tyre, color):
        self.typee = typee  # Public object instance attributes
        self.tyre = tyre
        self.color = color

    """
    to access or modify private attributes 
    we need to make a getter to acess.
    setter to modify the private attriubtes in python encapsulation
    """

    # getter
    def get_name(self):
        return self.__name


x = Factory("car", "tvs", "blue")
x.color = "red"  # color changed blue to red
print(x.color)
# print(x.__name) this is error accessing private attributes
print(x.get_name())
