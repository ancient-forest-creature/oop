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

    def make_withdrawl(self, amount):
        self.account_balance += -abs(amount)
        print(f"Withdrawl successful. Account balance for {self.first_name} {self.last_name} account ID({self.account_id}) is now {self.account_balance}")

    def display_user_balance(self):
        print(f"The balance for account {self.account_id} is: {self.account_balance}")
    
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        print(f"Funds of {amount} were transfered to {other_user.first_name} {other_user.last_name} from account {self.account_id}")
        self.make_withdrawl(amount)


nathan = User("Torgl", "Thorson", "tthorson@gmail.com")
print(nathan.account_id)
nathan.make_deposit(10000)
nathan.make_deposit(100000)
nathan.make_deposit(80000)
nathan.make_withdrawl(13000)
nathan.display_user_balance()
ilana = User("Freya","Njörðrsdaughter", "hotFreya@gmail.com")
ilana.make_deposit(56000)
ilana.make_deposit(603995)
ilana.make_withdrawl(13000)
ilana.make_withdrawl(25000)
ilana.display_user_balance()
nathan.transfer_money(ilana, 3700)

jdoe = User("John", "Doe", "jdoe@gmail.com")
jdoe.make_deposit(5000)
jdoe.make_withdrawl(1200)
jdoe.make_withdrawl(749)
jdoe.make_withdrawl(8.99)
jdoe.account_balance