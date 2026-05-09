class Bank:
    def __init__(self, bankName, amount):
        self.bankName = bankName
        self.amount = amount
        self.minWithdraw = 1000
        self.maxWithdraw = 25000

    def deposit(self, amount):
        self.amount += amount
        print(f"{amount} taka has been deposited. You now have {self.amount} taka")

    def withdraw(self, amount):
        if amount < self.minWithdraw:
            print(f"Sorry! You've to withdraw atleast {self.minWithdraw}")
        elif amount > self.maxWithdraw:
            print(f"Sorry! The max limit for withdraw is: {self.maxWithdraw}")
        else:
            if amount > self.amount:
                print(f"You can't withdraw {amount} taka, You only have {self.amount} taka left")
            else:
                self.amount -= amount
                print(f"{amount} taka has been withdrawn. You now have {self.amount} taka")

ific = Bank("IFIC", 5000)
ific.deposit(20000)
ific.withdraw(500)
ific.withdraw(30000)
ific.withdraw(10000)
ific.withdraw(17000)
