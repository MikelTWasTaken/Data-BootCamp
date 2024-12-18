# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !
from datetime import datetime
b_day = input('Please provide your birthday in the following format DD/MM/YYYY: ')
birth_date = datetime.strptime(b_day, "%d/%m/%Y")
current_date = datetime.now()
age = current_date.year - birth_date.year
if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):

    age -= 1

last_digit = age % 10 #to remove the 10's place


cake = [
"      ___iiiii___",
"     |:H:a:p:p:y:|",
"    __|___________|__",
"   |^^^^^^^^^^^^^^^^^|",
"   |:B:i:r:t:h:d:a:y:|",
"   |                 |",
"   ~~~~~~~~~~~~~~~~~~~"
]

def print_cake(candles_count):
    for line in cake:
        print(line)
    # Print the candles
    print(" " * 8 + "i" * candles_count)
if (birth_date.year % 4 == 0 and (birth_date.year % 100 != 0 or birth_date.year % 400 == 0)):
    print("Happy Birthday! Here's your cake (you were born in a leap year):")
    print_cake(last_digit)
    print()  # Blank line between the cakes
    print_cake(last_digit)
else:
    print("Happy Birthday! Here's your cake:")
    print_cake(last_digit)