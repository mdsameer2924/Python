# **Bank Account Setup**: Build a class `BankAccount` initialized with an `account_holder` and a starting `balance` (default to 0.0 if not provided).
# Add a method `deposit(amount)` that adds to the balance and returns the updated total.
class BankAccount:
    def __init__(self,account_holder,balance=0.0):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
sameer=BankAccount('mohd sameer')
zara=BankAccount('Zara Hayat')

print(f"{sameer.account_holder}'s balance: {sameer.balance}")
print()
print(f"{zara.account_holder}'s balance: {zara.balance}")

sameer.deposit(200)

print(f"{sameer.account_holder}'s balance: {sameer.balance}")
sameer.deposit(800)
print(f"{sameer.account_holder}'s balance: {sameer.balance}")
zara.deposit(10000)
print(f"{zara.account_holder}'s balance: {zara.balance}")
zara.deposit(299.9)
print(f"{zara.account_holder}'s balance: {zara.balance}")
