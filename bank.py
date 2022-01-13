import random, string

class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account_balance = 0
        self.account_id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        print(f"Account for {first_name} {last_name} has been created!")

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"Deposti successful. Account balance for {self.first_name} {self.last_name} account ID({self.account_id}) is now {self.account_balance}")
        return self

    def make_withdrawl(self, amount):
        self.account_balance += -abs(amount)
        print(f"Withdrawl successful. Account balance for {self.first_name} {self.last_name} account ID({self.account_id}) is now {self.account_balance}")
        return self

    def display_user_balance(self):
        print(f"The balance for account {self.account_id} is: {self.account_balance}")
        return self
    
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        print(f"Funds of {amount} were transfered to {other_user.first_name} {other_user.last_name} from account {self.account_id}")
        self.make_withdrawl(amount)
        return self


torgl = User("Torgl", "Thorson", "tthorson@gmail.com")
print(torgl.account_id)
torgl.make_deposit(10000).make_deposit(100000).make_deposit(80000).make_withdrawl(13000).display_user_balance()
freya = User("Freya","Njörðrsdaughter", "hotFreya@gmail.com")
freya.make_deposit(56000).make_deposit(603995).make_withdrawl(13000).make_withdrawl(25000).display_user_balance()
torgl.transfer_money(freya, 3700)

jdoe = User("John", "Doe", "jdoe@gmail.com")
jdoe.make_deposit(5000).make_withdrawl(1200).make_withdrawl(749).make_withdrawl(8.99).display_user_balance()