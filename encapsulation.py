class bankaccount:
    balance=0
    accname=""
    def __init__(self):
        pass
    def withdraw(self,amount):
        self.balance=self.balance-amount
        return self.balance

    def transfer(self,amount):
        self.balance=self.balance-amount
        return self.balance
    def deposit (self,amount,accname):
        self.balance+=amount
        self.accname=accname
        return self.balance
    def display(self):
        print("details are, balance:",self.balance,"name:",self.accname)

#creatin instances
ac1=bankaccount()
ac1.balance=300000
ac1.accname="Dan"
ac1.display()
