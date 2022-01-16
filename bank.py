import random, string

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposti successful. Account balance for account ID({self.id}) is now {self.balance}")
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance += -abs(amount)
            print(f"Withdrawl successful. Account balance for account ID({self.id}) is now {self.balance}")
        else:
            print(f"Account {self.id} has Insufficient Funds for this transaction!")
        return self
    
    def display_account_info(self):
        print(f"The balance for account {self.id} is: {self.balance}")
        print(f"the interest rate for account {self.id} is: {self.int_rate}")
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

class User:
    # class attibutes
    population = 0
    bank_name = "First Bank of Coding"
    all_accounts_id = []
    def __init__(self, first_name, last_name, email, age):
        if User.validate_age(age):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.age = age
            self.account = {"checking" : BankAccount(0.02, 400), "savings" : BankAccount(0.05, 1500)}
            User.population += 1
        else:
            print(f"{first_name} {last_name} is too young to open an account.")

    def transfer_money(self, other_user, amount):
        if BankAccount.can_withdraw(self.account["checking"].balance, amount):
           other_user.account["savings"].deposit(amount)
           print(f"Funds of {amount} were transfered to {other_user.first_name} {other_user.last_name} from account {self.account['savings'].id}")
           self.account["checking"].withdraw(amount)
        else:
            print(f"Account {self.account['savings'].id} has Insufficient Funds for this request!")           
        return self

    @classmethod
    def user_population(cls):
        print(f"{cls.bank_name} has {cls.population} customers.")

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"This bank's name is now: {cls.bank_name}!")

    @staticmethod
    def validate_age(age):
        is_valid = True
        if age < 18:
            is_valid = False
        return is_valid
    
torgl = User("Torgl", "Thorson", "tthorson@gmail.com", 52)
print(torgl.account["checking"].id)
torgl.account["checking"].deposit(10000).deposit(100000).deposit(80000).withdraw(13000).display_account_info()
freya = User("Freya","Njörðrsdaughter", "hotFreya@gmail.com", 1798183)
freya.account["savings"].deposit(37890)
freya.account["checking"].deposit(56000).deposit(603995).withdraw(13000).withdraw(25000).display_account_info()
torgl.transfer_money(freya, 3700)
torgl.transfer_money(freya, 37000000000)

jdoe = User("John", "Doe", "jdoe@gmail.com", 27)
jdoe.account["checking"].deposit(5000).withdraw(1200).withdraw(749).withdraw(8.99).display_account_info()


bankacct1 = BankAccount(.0145, 2500)
bankacct2 = BankAccount(.0219, 4200)

bankacct1.deposit(3200).deposit(287.33).deposit(66.60).withdraw(999).yield_interest().display_account_info()
bankacct2.deposit(1700).deposit(29276.23).withdraw(8.99).withdraw(327.55).withdraw(666).withdraw(4487.23).yield_interest().display_account_info()

BankAccount.print_accounts()