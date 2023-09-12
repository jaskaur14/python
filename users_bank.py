#SLOAN HELPED ME WITH THIS ASSIGNMENT THERE MAY BE SOME SIMILARITIES
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    #calls on bank account's instance methods
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self


    #displays user's account balance
    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self




class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
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
        
    

user_1 = User("Jasleen" , " jkaur@gmail.com")
user_1.make_deposit(2000).make_deposit(500).display_user_balance()

user_2 = User("Kaur" , "kaurj@gmail.com")
user_2.make_deposit(10000).display_user_balance().make_withdrawal(500).display_user_balance()