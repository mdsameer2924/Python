# 1.Student Record: Create a class named Student with an `__init__` constructor that accepts `name`, `roll_number`, and `marks`. 
# Write a method `display_info()` that prints these details neatly. Instantiate one student and call the method.

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display(self):
        print(f"Student name: {self.name}")
        print(f"Student's Roll number: {self.roll_no}")
        print(f"Student Marks: {self.marks}")

s1=Student('mohd sameer',21,80)
s2=Student('Sonu',32,70)
s2.roll_no+=4
print("tryign")
print(s2.roll_no) #easily modify and access 
s2.display()
s1.display()
