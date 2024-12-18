class BankAccount():
    def __init__(self, owner_name, accnt_num, balance=0):  # Default balance is 0
        self.owner_name = owner_name  
        self.accnt_num = accnt_num
        self.transactions = []  # List to store transaction data
        self.balance = balance
        self.transaction_count = 0  # Initialize the transaction counter

    def deposit(self, amount):
        self.balance += amount
        self.transaction_count += 1  # Increment transaction count
        self.transactions.append((self.transaction_count, f'You deposited {amount}.'))  # Add transaction with number
        self.show_balance()  # Show the updated balance
        return self

    def withdraw(self, amount):
        if amount <= self.balance:  # Check if enough balance is available
            self.balance -= amount
            self.transaction_count += 1  # Increment transaction count
            self.transactions.append((self.transaction_count, f'You withdrew {amount}.'))  # Add transaction with number
            self.show_balance()  # Show the updated balance
        else:
            print("Insufficient funds!")  # Handle case for insufficient funds
        return self

    def show_balance(self):
        print(f'Your current balance is {self.balance}')

    def show_transactions(self):
        print("Transaction History:")
        for trans in self.transactions:
            print(f"Transaction {trans[0]}: {trans[1]}")
        


# Create an object for the bank account
my_account = BankAccount('Mike', 156, 100)

# Perform some transactions
my_account.deposit(50)  # Deposit 50
my_account.deposit(20)  # Deposit 20
my_account.withdraw(10)  # Withdraw 10

# Show transaction history
my_account.show_transactions()  # Print all transactions
my_account.show_balance()

