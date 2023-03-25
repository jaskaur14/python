#SLOAN HELPED ME WITH THIS ASSIGNMENT THERE MAY BE SOME SIMILARITIES
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # (remember, instance attributes go here)
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance <= 0:
            self.balance -= 5
            print("insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
            return self
            print(self.balance)
        
    def display_account_info(self):
        print (f"Current Balance: {self.balance}")
        return self
        
    def yield_interest(self):
        self.balance = (self.balance * int_rate) + self.balance
        return self
        
Jasleen = BankAccount(0.01, 10000)
Jasleen.deposit(2000).deposit(100).deposit(300).withdraw(500).display_account_info()

Kaur = BankAccount(0.02, 50000)
Kaur.deposit(100).deposit(7000).withdraw(200).withdraw(700).withdraw(2000).withdraw(900).display_account_info()