# Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:

# 18,22,24
import math

# Constants
C = 50
H = 30

d_values = input("Enter comma-separated values for D: ").split(',')

results = []
for d in d_values:
    d = d.strip()  
    if d: 
        D = int(d)  
        Q = int(math.sqrt((2 * C * D) / H))  
        results.append(Q)

print(",".join(map(str, results)))


# Exercise 2 : List of integers
# Instructions
# Given a list of 10 integers to analyze. For example:
#
#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

L1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
L2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
L3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
L4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# Store the list of numbers in a variable.
new_list = L1 + L2 + L3 + L4
# Print the following information:
# a. The list of numbers – printed in a single line
print("The list of numbers:", new_list) 
# b. The list of numbers – sorted in descending order (largest to smallest)
print("List sorted in descending order:", sorted(new_list, reverse=True))
# c. The sum of all the numbers
print("Sum of all numbers:", sum(new_list))
# A list containing the first and the last numbers.
print([new_list[0], new_list[-1]])
# A list of all the numbers greater than 50.
print([num for num in new_list if num > 50])
# A list of all the numbers smaller than 10.
print([num for num in new_list if num < 10])
# A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
print([num**2 for num in new_list])
# The numbers without any duplicates – also print how many numbers are in the new list.
unique_numbers = list(set(new_list))
print(unique_numbers) 
print(f"The number of unique elements is: {len(unique_numbers)}")
# The average of all the numbers.
avg = sum(new_list) / len(new_list)
print(avg)
# The largest number.
print(max(new_list))
# 10.The smallest number.
print(min(new_list))

# Exercise 3: Working on a paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
note = "In The Hitchhiker's Guide to the Galaxy series, specifically in Mostly Harmless, Arthur Dent, one of the main characters, eventually finds himself stranded on a primitive planet. There, he makes a humble life for himself by perfecting the art of making sandwiches. Initially, the locals see bread as merely a basic food, but Arthur's craftsmanship turns sandwich-making into something of an art form. Over time, he becomes something of a local legend for his sandwich-making skills, bringing a small slice of his old Earth life into a world that is otherwise unfamiliar and harsh. His sandwiches symbolize a kind of quiet resistance to the chaotic universe, reminding him of the comforts of home and the beauty in small, meaningful acts."
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many unique words it contains.
sentence_count = note.count('.') 
print(f"The paragraph contains {sentence_count} sentences.")

words = note.split()  # Split by spaces to count words
word_count = len(words)
print(f"The paragraph contains {word_count} words.")


# Exercise 4 : Frequency Of The Words
# Instructions
# Write a program that prints the frequency of the words from the input.
note2 = input('Please write a few sentences about a relative or rolemodel: ')
n2_count = {}

words = note2.split()
for w in words:
    word = words.lower()
    if word in n2_count:
        n2_count[word] +=1
    else:
        n2_count[word] == 1

print(n2_count)


# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1