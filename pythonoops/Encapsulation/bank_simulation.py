# ATM PIN Protection: Build a class BankAccount with a private balance __balance and a private PIN __pin.
# Provide a method verify_pin(entered_pin) that returns True if it matches, and 
# a method withdraw(amount, pin) that only permits withdrawal if the correct PIN is provided and the balance is sufficient.

class BankAccount:
    def __init__(self,balance,pin):
        self.__balance=balance
        self.__pin=pin
    def verify_pin(self,entered_pin):
        if entered_pin==self.__pin:
            return True
    def withdraw(self,amount,pin):
        if amount<=self.__balance and self.__pin==pin:
            self.__balance-=amount
            return f"Withdrawl amount: {amount}\nAvaiable bal: {self.__balance}"
    def check_balance(self):
        print(f"Current Balance: {self.__balance}")
    
c1=BankAccount(1000,1234)

# print(c1.verify_pin(1234))

# show_balance=c1.check_balance()
# print(show_balance)
# print(c1.withdraw(300,1234))

# print(c1.check_balance())
# c1.withdraw(10,1234)
# print(c1.check_balance())