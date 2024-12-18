#CLASS ATTRIBUTES

# You can also define an attribute that belongs to the class and not to each instance; it’s called a class attribute. Anything assigned in the class scope is a class attribute – every instance of the class shares the same one. For example, let’s define the name of dogs king as a class attribute:

class Dog():
    dogs_king = "Bernie IV" #class attribute (shared by all instances)

    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print(f"{self.name} barks ! WAF")

    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters")

    def rename(self, new_name):
        self.name = new_name

my_dog = Dog("Rex")
my_dog.rename("Paul")

# The dogs_king variable is now defined as “Bernie IV”, we don’t need to have a Dog object to call this variable; use:
# print("The king of the dogs is:", Dog.dogs_king)
# For example, we can save the number of dogs ever created in a class variable and increment it each time a dog is made (in the __init__ function).

class Dog():
    number_of_dogs = 0 #class Attribute
    dogs_king = "Bernie IV" #class Attribute

    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog
        # Increment the number of dogs
        Dog.number_of_dogs += 1

    def bark(self):
        print(f"{self.name} barks ! WAF")

    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters")

    def rename(self, new_name):
        self.name = new_name

my_dog = Dog("Rex")
my_dog2 = Dog("Bernie V")
print(f"Curently, there are {Dog.number_of_dogs} dogs")


# In this code:

# Class Attributes: number_of_dogs and dogs_king are shared by all Dog instances. They belong to the class itself, not to any one dog.

# number_of_dogs keeps track of how many dogs have been created. Every time a new Dog is made, it goes up by 1.
# dogs_king is a title for the "king" of all dogs, set to "Bernie IV" here. All dogs share this value.
# Instance Attributes: These are unique to each dog. For example, name is an instance attribute, so my_dog and my_dog2 each have their own names ("Rex" and "Bernie V").

# Example
# Creating my_dog = Dog("Rex") sets my_dog's name to "Rex" and increases Dog.number_of_dogs to 1.
# Creating my_dog2 = Dog("Bernie V") gives it the name "Bernie V" and increases Dog.number_of_dogs to 2.
# When you print Dog.number_of_dogs, it shows 2, the total number of dogs created so far.

############################################################################

#FOR THE CLASS ATTRIBUTES OF BANK ACCOUNT
class BankAccount():
    # Class Attributes
    bank_name = "Global Bank"  # Shared bank name for all accounts
    total_accounts = 0  # Count of all accounts created

    def __init__(self, owner_name, accnt_num, balance=0):  # Default balance is 0
        self.owner_name = owner_name  
        self.accnt_num = accnt_num
        self.transactions = []  # List to store transaction data
        self.balance = balance
        self.transaction_count = 0  # Initialize the transaction counter

        # Increment the total number of accounts
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount
        self.transaction_count += 1  # Increment transaction count
        self.transactions.append((self.transaction_count, f'You deposited {amount}.'))  # Add transaction with number
        self.show_balance()  # Show the updated balance

    def withdraw(self, amount):
        if amount <= self.balance:  # Check if enough balance is available
            self.balance -= amount
            self.transaction_count += 1  # Increment transaction count
            self.transactions.append((self.transaction_count, f'You withdrew {amount}.'))  # Add transaction with number
            self.show_balance()  # Show the updated balance
        else:
            print("Insufficient funds!")  # Handle case for insufficient funds

    def show_balance(self):
        print(f'Your current balance is {self.balance}')

    def show_transactions(self):
        print("Transaction History:")
        for trans in self.transactions:
            print(f"Transaction {trans[0]}: {trans[1]}")

    @classmethod
    def show_bank_info(cls):
        print(f"Bank Name: {cls.bank_name}")
        print(f"Total Accounts: {cls.total_accounts}")
    

# Create an object for the bank account
my_account = BankAccount('Mike', 156, 100)

# Perform some transactions
my_account.deposit(50)  # Deposit 50
my_account.deposit(20)  # Deposit 20
my_account.withdraw(10)  # Withdraw 10

# Show transaction history
my_account.show_transactions()  # Print all transactions
my_account.show_balance()

# Create another bank account
another_account = BankAccount('Sarah', 157, 200)

# Perform transactions on this new account
another_account.deposit(100)  # Deposit 100
another_account.withdraw(50)  # Withdraw 50

# Show transaction history for this new account
another_account.show_transactions()

# Show balance for this new account
another_account.show_balance()

# Show bank information (class-level details)
BankAccount.show_bank_info()


# Explanation
# Class Attribute bank_name: This stores the name of the bank, and it’s the same for all bank accounts.

# Class Attribute total_accounts: This keeps track of the total number of BankAccount instances created. Every time a new BankAccount is created, it increments by 1 in the __init__ method.

# Class Method show_bank_info: This method is called on the class (not an instance) to display the bank name and total number of accounts.

# Usage
# When you create a new BankAccount, total_accounts increases, and show_bank_info shows the bank’s name and total accounts.

# This keeps your code simple and helps you track information at the class level.
