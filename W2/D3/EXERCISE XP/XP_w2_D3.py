
# 🌟 Exercise 1: Currencies
# Instructions
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
         return f"{self.amount} {self.currency}s"
        
    def __int__(self):
        return self.amount
    
    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __add__(self, other):
        if isinstance (other, Currency):
            if self.currency == other.currency:
                return Currency(self.currency, self.amount + other.amount)
            else:
                raise TypeError (f'cannot add between currencies {self.currency} and {other.currency}')
        elif isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError("Unsupported type for addition")
        
    def __add__(self, int):
        if isinstance (int, Currency):
            if self.currency == int.currency:
                return Currency(self.currency, self.amount + int.amount)
            else:
                raise TypeError (f"cannot add between currencies that don't exist")

# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1.__str__)
# >>> str(c1)
# '5 dollars'
print(c1.__int__)
# >>> int(c1)
# 5
print(c1.__repr__)
# >>> repr(c1)
# '5 dollars'
print(c1+(5).__add__)
# >>> c1 + 5
# 10
print(c1+(c2).__add__)
# >>> c1 + c2
# 15
print(c1+(5).__add__)
# >>> c1 += 5
# >>> c1
# 10 dollars
print(c1+(c2).__add__)
# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>


# 🌟 Exercise 2: Import
# Instructions
# In a file named func.py create a function that sum 2 numbers, and prints the result
# In a file named exercise_one.py import the function and call it to print the result
# Hint: You can use the the following syntaxes:

# import module_name 

# OR 

# from module_name import function_name 

# OR 

# from module_name import function_name as fn 

# OR

# import module_name as mn


# 🌟 Exercise 3: String module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import random
import string

def generate_random_string (len=5):
    letters = string.ascii_letters 
    random_string = " ".join(random.choice(letters)for i in range(len))   
    return random_string
print(generate_random_string())     

# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.
from datetime import datetime
def generate_today_date():
    today = datetime.today().date()
    return today
print(generate_today_date())

# Exercise 5 : Amount of time left until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).
from datetime import datetime

def time_until_new_year():
    now = datetime.now()
    
    new_year_date = datetime(now.year + 1, 1, 1)
    
    time_left = new_year_date - now
    
    days = time_left.days
    total_seconds = time_left.seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return f"The 1st of January is in {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds."
print(time_until_new_year())


# Exercise 6 : Birthday and minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

from datetime import datetime, date

class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday  # Expecting a date object instead of a string

    def minutes_lived(self):
        now = datetime.now()
        minutes = (now - datetime.combine(self.birthday, datetime.min.time())).days * 24 * 60  # Days to hours to minutes
        return minutes

# Example usage
person1 = Person('Mike', date(1992, 6, 4))  # Passing date directly
print(f"{person1.name} has lived about {person1.minutes_lived()} minutes.")

# Exercise 7 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

#I don't know how to do a faker module. 