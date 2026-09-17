# Create Account class with 2 attr - balance and acc.no 
class Account:
    def __init__(self,balance,account_No):
        self.balance = balance
        self.acc_no = account_No
    # Debit method:
    def debit(self,amount):
        self.balance -= amount
        print(f"{amount} Rs was debited to your account ({self.acc_no} acc.no)")
    # credit method:
    def credit(self,amount):
        self.balance += amount
        print(f"{amount} Rs was credited to your account ({self.acc_no} acc.no)")
    # Final balance:
    def final_bal(self):
        print(f"Now you balance is {self.balance} Rs")


ayra = Account(250000 , 2235)
ayra.debit(40000)
ayra.credit(24000)
ayra.final_bal()

