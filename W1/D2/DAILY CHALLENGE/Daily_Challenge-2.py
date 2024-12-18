# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

#reference notes:
# #WHILE Loops
# While loops differ from for loops, they have what we call an indefinite iteration cycle. What that means is that the number of times they execute isn’t defined by the length of a given list but by a specific breakpoint that will stop the loop’s execution when it is hit.
# A while loop is defined somewhat similarly to a conditional statement. The loop will keep running as long as the set condition is True and stop when this condition evaluates to False.
# The while loop runs as long as (or while) a certain condition is true.
# It will execute all the instructions in the loop, then test the condition, if the condition is still True, it will rerun the loop, and again until the condition becomes false.

# my_nums = [1,2,3,4,5,6,77]
# print(sum(my_nums)) #this is the fastest way to do it

# output = 0 #this is what happens behind the scenes of print(sum(my_nums)) above.
# for i in range (len(my_nums)):
#     output += my_nums[i]
#     print(output)
# #attempt 1
# number = int(input("give me a number please: ")) #input needed because we are asking someone for something and need a value in return.
# length = int(input("how long is the list? ")) #ditto above

# list_of_multiples = [] #need to define a list from instructions. Multiples mean whatever number we give will be multiplied by itself. The length indicates how long that list will be.
# for i in range (length +1): #for i in range is probably what we need here because we have a range of data that needs to be looped through
#       list_of_multiples.append(number)
# print(list_of_multiples)

#I keep getting the same number repeated by the length of the list. I need to multiply something but can't figure out where.
# EXAMPLE: 
#give me a number please: 7
# how long is the list? 9
# [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]

# #attempt 2 after watching https://www.youtube.com/watch?v=3dt4OGnU5sM
# list_of_multiples = [number*number for i in length]
# length = int(input("how long is the list? "))
# number = int(input("give me a number please: "))
# print(list_of_multiples)

#final attempt:
number = int(input("give me a number please: "))
length = int(input("how long is the list? "))

list_of_multiples = [number * i for i in range(1, length + 1)]

print(list_of_multiples)


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

users_word = input("Give a word with repeating letters: ")
new_string = users_word[0]
for i in range(1, len(users_word)):
    if users_word[i] != users_word[i-1]:
        new_string += users_word[i]
print("New string without consecutive duplicates:", new_string)