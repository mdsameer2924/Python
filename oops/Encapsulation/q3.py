# Employee Salary Control: Design an Employee class with a public name and a private __salary.
# Write a getter method to view the salary and a setter method to update it, ensuring that a negative salary cannot be assigned.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        if salary<0:
            print("cannot be assigned")
            salary=0
            self.__salary=salary
        self.__salary=salary

    ## getter salary via method
    def show_salary(self):
        return self.__salary

    ## setter update the salary via methods
    def give_salary(self,amt):
        if self.amt<0:
            self.__salary=0
            return f"salary setted to {self.__salary}\nBecause negative salary cannot be assigned error"
        self.__salary+=amt
        return self.__salary


emp=Employee('sameer',5000)
emp.__salary=8000
print(emp.show_salary())
print(emp.name)
