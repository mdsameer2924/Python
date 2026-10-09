# Employee Salary Control: Design an Employee class with a public name and a private __salary.
# Write a getter method to view the salary and a setter method to update it, ensuring that a negative salary cannot be assigned.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    ## getter salary via method
    def show_salary(self):
         print(f"Salary: {self.__salary}")

    ## setter update the salary via methods
    def give_salary(self,amt):
        if amt<0:
            return "Salary can't be negative"
        self.__salary+=amt
        return self.__salary


e1=Employee('Sameer',2000)
e1.show_salary()
e1.give_salary(4599)
e1.show_salary()
print(e1.give_salary(-3434))
       