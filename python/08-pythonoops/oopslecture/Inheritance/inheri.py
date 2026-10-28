class Human:
    ## Constructor
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.__age = "not defined"  # private attributes

    # Methods
    def display_info(self):
        print(f"Name: {self.name} Gender: {self.gender} Age: {get_age()}")

    ## Setter
    def set_age(self, age):
        self.__age = age

    ## Getter
    def get_age(self):
        return self.__age


class Employee(Human):  ## Child class inherit Human
    ## Constructor
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, gender)  # super helps to take attributes from parents
        super.set_age(age)
        self.empid = emp_id
        self.salary = salary

    ## Method override
    def display_info(self):
        # return super().display_info()
        print(
            f"Name: {self.name} Age: {super().get_age()} Employee Id: {self.empid} Salary: {self.salary}"
        )


e = Employee("sameer", 20, 101, 80000)
e.display_info()
