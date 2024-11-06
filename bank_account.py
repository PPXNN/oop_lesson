class AccountDB:
    def __init__(self):
        self.account_database = []

    def create_account(self, account):
        index = self.search_account_db(account.account_number)
        if index == -1:
            self.account_database.append(account)
        else:
            print("Account", account.account_number, "already exists")

    def delete_account(self, num):
        index = self.search_account_db(num)
        if index != -1:
            print("Deleting account:", self.account_database[index]["account_number"])
            del self.account_database[index]
        else:
            print(num, "invalid account number; nothing to be deleted.")

    def search_account_db(self, num):
        for i in range(len(self.account_database)):
            if self.account_database[i].account_number == num:
                return i
        return -1

    def search_public(self, account_num):
        for account in self.account_database:
            if account.account_number == account_num:
                return account
        return None

    def deposit(self, account_num, amount):
        account = self.search_public(account_num)
        if account:
            account.deposit(amount)

    def withdraw(self, account_num, amount):
        account = self.search_public(account_num)
        if account:
            account.withdraw(amount)

    def show_account(self, account_num):
        account = self.search_public(account_num)
        if account:
            print(f"Showing details for {account.account_number}: {account}")

    def __str__(self):
        s = ''
        for account in self.account_database:
            s += str(account) + ", "
        return s


class Account:
    def __init__(self, num, type, account_name, balance):
        self.account_number = num
        self.type = type
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def __str__(self):
        return '{' + str(self.account_number) + ',' + str(self.type) + ',' + str(self.account_name) + ',' + str(
            self.balance) + '}'


account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)
account4 = Account("0004", "saving", "David Wood", 4000)
account5 = Account("0004", "saving", "David Wood", 4000)
my_db = AccountDB()
my_db.create_account(account1)
my_db.create_account(account2)
my_db.create_account(account3)
my_db.create_account(account4)
my_db.create_account(account5)
print(my_db)
my_db.show_account('0003')
my_db.deposit('0003', 50)
my_db.show_account('0003')
my_db.withdraw("0003", 25)
my_db.show_account('0003')
my_db.show_account('0003')
my_db.deposit('0003', 50)
my_db.withdraw("0001", 6000)