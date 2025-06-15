class BankAccount:
    def __init__(self, account_balance):
        """This is the existing amount in bank account"""
        if account_balance < 0:
            print("Account balance cannot be negative. Initializing 0 balance.")
            self.account_balance = 0
        else:
            print(f"Account opening balance: KES {self.account_balance:.2f}")
 
    def display_balance (self, display_balance):        
        print(f"Current balance: KES {self.account_balance:.2f}")
        self.display_balance ()

    def deposit(self, amount):
        """Deposits into the bank account"""
        if amount > 0:
            self.account_balance += amount
            print(f"Amount Deposited: KES {self.amount:.2f}")
            return True
        else:
            print("Deposit amount must be positive")
            return False

    def withdraw(self, amount):
        """Withdraws specified ammount from bank account"""
        if amount <= 0:
            print("Withdrawal must be positive")
        elif self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Amount withdrawn: KES {amount:.2f}")
        else:
            print("Transcation Failed. Insufficient Funds!")
            

    


        
