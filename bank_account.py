import random, string

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.account_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposti successful. Account balance for account ID({self.account_id}) is now {self.balance}")
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance += -abs(amount)
            print(f"Withdrawl successful. Account balance for account ID({self.account_id}) is now {self.balance}")
        else:
            print(f"Account {self.account_id} has Insufficient Funds for this transaction!")
        return self
    
    def display_account_info(self):
        print(f"The balance for account {self.account_id} is: {self.balance}")
        print(f"the interest rate for account {self.account_id} is: {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            earned_int = self.balance * self.int_rate
            self.balance = round (self.balance + earned_int, 2)
            print(f"you account earned {earned_int} in interest for a total balance of: {self.balance}")
        else:
            print("You can't earn interest on a negitive balance")
        return self

    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

bankacct1 = BankAccount(.0145, 2500)
bankacct2 = BankAccount(.0219, 4200)

bankacct1.deposit(3200).deposit(287.33).deposit(66.60).withdraw(999).yield_interest().display_account_info()
bankacct2.deposit(1700).deposit(29276.23).withdraw(8.99).withdraw(327.55).withdraw(666).withdraw(4487.23).yield_interest().display_account_info()

BankAccount.print_accounts()