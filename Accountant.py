class BankAccount:
    def __init__(self,owner:str,balance:int):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,money):
        self.balance =  self.balance + money
        return f" You have deposited {money} balance is now,{self.balance}"
    
    def withdraw(self,money):
      if money > self.balance:
            print (f"Your balance is {self.balance} and it is not enough to withdraw {money}")
      else:
          self.balance =  self.balance - money
          return f" You have withdrawn {money} your balance is now,{self.balance}. Funds Unavailable"
    
account1 = BankAccount("Sarah",1000)
    
account2 = BankAccount("Jimoh",10000)

print(f"{account1.owner} you have {account1.balance}")

print(account1.deposit(50))
print()
# print(f"{account1.owner} you now have {account1.balance}")
print(account1.withdraw(500))
print()
print(account1.withdraw(5000))
