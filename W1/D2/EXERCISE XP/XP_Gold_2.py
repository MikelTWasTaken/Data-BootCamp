# Exercise 1: Concatenate lists
# Instructions
# Write code that concatenates two lists together without using the + sign.
list_1 = [1,2,3,4,5,6]
list_2 = ['a','b','c','d','e','f']

combine = list_1+list_2
print(combine)

# Exercise 2: Range of numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
a = int(1500)
b = int(2500)

c=a%5 #add enough to get to the next multiple of 5

multiples = []
multiples2 = []

for value in range(a+5-c, b+1,5):
    multiples.append(value)

for value in range(a+7-c, b+1,7):
    multiples2.append(value)

print(multiples)
print(multiples2)

# Exercise 3: 
# Check the index
# Instructions
# Using this variable

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

guess_who = input('What is your name? ')

while guess_who:
    if guess_who in names:
        print(f"The index of the first occurrence of {guess_who} is {names.index(guess_who)}")
        break    
    else:
        print(f'Name not found in list')
        guess_who = input('What is your name? ')


# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87

#     The greatest number is: 87
a = int(input("Input the 1st number: "))
b = int(input("Input the 2nd number: "))
c = int(input("Input the 3rd number: "))

greatest = max(input(a, b, c))

print(f'The greatest number is{greatest}')

# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

#create a string with all letters in alpha
#
import string
string_unfiltered = string.ascii_lowercase
vowels = {'a','e','i','o','u'}

for letter in string_unfiltered:
    if letter in vowels:
        print(f'{letter} is the vowel you are looking for.')
    else:
        print(f'{letter} is a consonant.')



# Exercise 6: Words and letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
words = []
for i in range(7):
    word = input(f"Please provide word {i + 1}: ")
    words.append(word)

letter = input("Please provide a single letter: ")
for word in words:
    if letter in word:
        print(f"The letter '{letter}' is found in '{word}' at index {word.index(letter)}.")
    else:
        print(f"The letter '{letter}' does not exist in the word '{word}'.")



# Exercise 7: Min, Max, Sum
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.
nums = list(range(1,1000001))

high = max(nums)
low = min(nums)
calc = sum(high,low)
print(high)
print(low)
print(calc)

# Exercise 8 : List and Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

more_nums = input('Please provide sequence of comma-separated numbers: ')

list = []
tuple = ()

num_list = more_nums.split(",")
num_tuple = tuple(num_list)

print("List:", num_list)
print("Tuple:", num_tuple)


# Exercise 9 : Random number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.
import random
all_nums = int(input("Please enter a number from 1 to 9: "))
rand_num = random.uniform(0,9)

while True:
    if all_nums == rand_num:
        print(f"You've guessd the correct number!")
        break
    else:
        print(f'Wrong, guess again!')
        all_nums = int(input("Please enter a number from 1 to 9: "))
