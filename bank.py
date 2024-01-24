# یک برنامه ساده مدیریت بانک



class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def display_info(self):
        print(f"customer : {self.name}")
        self.account.display_balance()

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} dollar was accepted")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} dollar withraw accepted.")
        else:
            print("not enough balance in your account ")

    def display_balance(self):
        print(f" {self.balance} dollar do you have ")

# ساخت حساب بانکی
account1 = BankAccount()

# ساخت مشتری
customer1 = Customer("nima", account1)

# نمایش اطلاعات مشتری و حساب
customer1.display_info()

# واریز و برداشت از حساب
account1.deposit(1000)
account1.withdraw(500)

# نمایش اطلاعات بعد از تغییرات
customer1.display_info()
