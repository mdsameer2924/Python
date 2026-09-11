import oops.Encapsulation.bank_simulation as bank

bal=bank.c1
bal.check_balance()
print(bal.verify_pin(1234))
bal.withdraw(403,1234)
bal.check_balance()