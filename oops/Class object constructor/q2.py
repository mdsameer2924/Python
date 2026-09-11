# Rectangle Geometry: Design a class Rectangle that takes width and height in its constructor.
#  Add a method calculate_area() that returns the area (width * height) and a method `calculate_perimeter()` that returns the perimeter (2 * (width + height)).
class Rectangle: #class
    def __init__(self,width,height): #constructor
        self.width=width
        self.height=height
    def calculate_area(self): #methods
        print(f"Your given width: {self.width}cm")
        print(f"Your given Height: {self.height}cm")
        print()
        print(f"Area of Rectangle: {self.width*self.height}cm")

    def calculate_perimeter(self):   #methods
        print(f"Your given width: {self.width}cm")
        print(f"Your given Height: {self.height}cm")
        print()
        print(f"Perimeter of Rectangle: {2*(self.width+self.height)}cm")

rec=Rectangle(40,50) #object
rec.calculate_area()
rec.calculate_perimeter()

