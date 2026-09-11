# ATM PIN Protection: Build a class BankAccount with a private balance __balance and a private PIN __pin.
# Provide a method verify_pin(entered_pin) that returns True if it matches, and 
# a method withdraw(amount, pin) that only permits withdrawal if the correct PIN is provided and the balance is sufficient.

class BankAccount:
    def __init__(self,balance,pin):
        self.__balance=balance
        self.__pin=pin

    def verify_pin(self,entered_pin):
        return entered_pin==self.__pin

    def withdraw(self,amount,pin):
        if not self.verify_pin(pin):
            return "wrong pin try again"
        if amount>self.__balance:
            return "insufficient balance"
        self.__balance-=amount
        return f"Withdrawal amount: {amount}\nAvailable bal: {self.__balance}"

s2=BankAccount(5000,2924)
s2.verify_pin(3459)
