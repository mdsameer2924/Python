"""
Exercise 1. Arithmetic Product and Conditional Logic
Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000,
return their product; otherwise, return their sum.

Exercise Purpose: Learn basic control flow and the use of if-else statements. Understand how code decisions change output based on a mathematical threshold.

Given Input:

Case 1: number1 = 20, number2 = 30
Case 2: number1 = 40, number2 = 30
Expected Output:

The result is 600
The result is 70

reference: https://pynative.com/python-basic-exercise-for-beginners/#:~:text=Exercise%201.%20Arithmetic%20Product%20and%20Conditional%20Logic,-Practice%20Problem%3A
"""


# def product_condition(num1, num2):
#     if (num1 * num2) <= 1000:
#         return num1 * num2
#     elif (num1 * num2) >= 1001:
#         return num1 + num2
#     else:
#         return "invalid input try again!"
#
#
# case1 = product_condition(30, 20)
# case2 = product_condition(40, 30)
# print(f"Case 1: {case1}")
# print(f"Case 2: {case2}")


class Arithmetic:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def product_or_sum(self):
        product = self.num1 * self.num2
        if product <= 1000:
            return self.num1 * self.num2
        elif product >= 1001:
            return self.num1 + self.num2
        else:
            return "invaild input try to give input as a number"

    def __str__(self) -> str:
        return f"{self.product_or_sum()}"


case1 = Arithmetic(20, 30)
case2 = Arithmetic(40, 30)
print("Case 1: ", case1)
print("Case 2: ", case2)
