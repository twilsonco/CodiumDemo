# Python

class Account:
    def __init__(self, account_type, starting_balance=0):
        self.account_type = account_type
        if account_type == 'savings':
            self.minimum_balance = 500
        elif account_type == 'checking':
            self.minimum_balance = 100
        else:
            print('Invalid account type')
        self.balance = max(self.minimum_balance, starting_balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Cannot withdraw, minimum balance requirement')
        else:
            self.balance -= amount

account1 = Account('savings', 1000)
account1.deposit(1000)
account1.withdraw(200)
print(account1.balance)

account2 = Account('checking', 500)
account2.deposit(500)
account2.withdraw(200)
print(account2.balance)