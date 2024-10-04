class BankAccount :
    def __init__(self,account_balance=0):
        self.account_balance = account_balance
    def deposit(self,amount) :
        self.account_balance += amount
    def withdraw(self,amount):
        try:
            if amount>0:
                self.account_balance-=amount
            else:
                return f"the amount added must be a positive number"
        except TypeError:
            return f"the input is invalid. Please enter a number"
    def display_balance (self):
        return f"Current Balance: ${self.account_balance}"


        