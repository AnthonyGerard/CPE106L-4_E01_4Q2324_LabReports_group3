# savingsaccount.py
 
class SavingsAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return f"Name: {self.name}, PIN: {self.pin}, Balance: ${self.balance}"
 
# bank.py
import pickle
import random

from savingsaccount import SavingsAccount
 
class Bank:
    def __init__(self, fileName=None):
        self.accounts = {}
        self.fileName = fileName
        
        if fileName:
            with open(fileName, 'rb') as fileObj:
                while True:
                    try:
                        account = pickle.load(fileObj)
                        self.add(account)
                    except EOFError:
                        break
    
    def __str__(self):
        sorted_accounts = sorted(self.accounts.values(), key=lambda acc: acc.get_name())
        result = "Bank Accounts (ordered by name):\n"
        for account in sorted_accounts:
            result += str(account) + "\n"
        return result
    
    def make_key(self, name, pin):
        return name + "/" + pin
    
    def add(self, account):
        key = self.make_key(account.get_name(), account.pin)
        self.accounts[key] = account
    
    def remove(self, name, pin):
        key = self.make_key(name, pin)
        return self.accounts.pop(key, None)
    
    def get(self, name, pin):
        key = self.make_key(name, pin)
        return self.accounts.get(key, None)
    
    def compute_interest(self):
        total_interest = 0
        for account in self.accounts.values():
            total_interest += account.compute_interest()
        return total_interest
    
    def get_keys(self):
        return sorted(self.accounts.keys())
    
    def save(self, fileName=None):
        if fileName:
            self.fileName = fileName
        elif not self.fileName:
            return
        
        with open(self.fileName, 'wb') as fileObj:
            for account in self.accounts.values():
                pickle.dump(account, fileObj)
                

def create_bank(num_accounts=1):
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia", "Ken", "Jill", "Jack")
    bank = Bank()
    upper_pin = num_accounts + 1000
    for pin_number in range(1000, upper_pin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pin_number), balance))
    return bank
 
def test_account():
    account = SavingsAccount("Ken", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.get_balance())
    print(account.deposit(-50))
    print("Expect 600:", account.get_balance())
    print(account.withdraw(100))
    print("Expect 500:", account.get_balance())
    print(account.withdraw(-50))
    print("Expect 500:", account.get_balance())
    print(account.withdraw(100000))
    print("Expect 500:", account.get_balance())
 
def main(number=10, fileName=None):
    test_account()

from bank import Bank, createBank
 
def main():
    bank = create_bank(5)
    print(bank)
 
if __name__ == "__main__":
    main()
