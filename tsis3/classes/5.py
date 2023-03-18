class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, income):
        def __init__ (self, income):
            self.newcome = income
        self.balance += income

    def withdraw(self, outcome):
        def __init__(self, outcome):
            self.outcome = outcome
        if self.balance >= outcome:
            self.balance -= outcome
        else:
            self.balance = 0

    def show(self):
        print(self.balance)


a = BankAccount("Amina", 5000)
a.deposit(100)
a.withdraw(1500)
a.show()