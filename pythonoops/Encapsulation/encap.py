class Money:
    def __init__(self,owner,init_bal):
        self.owner=owner
        self.__balance=init_bal

    # only acces private attributed using getter method
    def get_balance(self):
        return self.__balance,self.owner

    ## setter method to modify the private attributes
    def deposit(self,amount):
        self.__balance+=amount
        return self.__balance

acc=Money('sameer',1000)
# print(acc.get_balance())
print(acc.get_balance())
acc.owner='Ayan'
acc.deposit(39)
print(acc.get_balance())