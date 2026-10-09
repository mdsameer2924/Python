# Create a parent class named Employee with an __init__ that accepts name and salary, plus a method get_details() that returns the name and salary.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def get_details(self):
        return f"name: {self.name}\nSalary: {self.salary}"

class manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def show_dep(self):
        return self.department
    def get_details(self):
        return super().get_details()

c=manager('Sameer',9000,'IT')
print(c.get_details(),c.show_dep())