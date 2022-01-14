import random, string

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
            self.account_balance = 0
            self.account_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            User.population += 1
            print(f"Account for {first_name} {last_name} has been created!")
        else:
            print(f"{first_name} {last_name} is too young to open an account.")


    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"Deposti successful. Account balance for {self.first_name} {self.last_name} account ID({self.account_id}) is now {self.account_balance}")
        return self

    def make_withdrawl(self, amount):
        if User.can_withdraw(self.account_balance, amount):
            self.account_balance += -abs(amount)
            print(f"Withdrawl successful. Account balance for {self.first_name} {self.last_name} account ID({self.account_id}) is now {self.account_balance}")
        else:
            print(f"Account {self.account_id} has Insufficient Funds for this request!")
        return self

    def display_user_balance(self):
        print(f"The balance for account {self.account_id} is: {self.account_balance}")
        return self
    
    def transfer_money(self, other_user, amount):
        if User.can_withdraw(self.account_balance, amount):
           other_user.make_deposit(amount)
           print(f"Funds of {amount} were transfered to {other_user.first_name} {other_user.last_name} from account {self.account_id}")
           self.make_withdrawl(amount)
        else:
            print(f"Account {self.account_id} has Insufficient Funds for this request!")           
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
    
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

torgl = User("Torgl", "Thorson", "tthorson@gmail.com", 52)
print(torgl.account_id)
torgl.make_deposit(10000).make_deposit(100000).make_deposit(80000).make_withdrawl(13000).display_user_balance()
freya = User("Freya","Njörðrsdaughter", "hotFreya@gmail.com", 1798183)
freya.make_deposit(56000).make_deposit(603995).make_withdrawl(13000).make_withdrawl(25000).display_user_balance()
torgl.transfer_money(freya, 3700)
torgl.transfer_money(freya, 37000000000)

jdoe = User("John", "Doe", "jdoe@gmail.com", 27)
jdoe.make_deposit(5000).make_withdrawl(1200).make_withdrawl(749).make_withdrawl(8.99).display_user_balance()