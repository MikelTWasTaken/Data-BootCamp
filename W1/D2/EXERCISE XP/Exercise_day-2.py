#EX 1
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

friend_fav_numbers = {5,6,7,8,9,0}
my_fav_numbers = {4,7,99,20,24,66}
my_fav_numbers.add (100)
my_fav_numbers.add (80)
print(my_fav_numbers)

my_fav_numbers = {4,7,99,20,24,66}
x =  my_fav_numbers.pop()
print(x)
print(my_fav_numbers)

my_fav_numbers.update(friend_fav_numbers)
print(my_fav_numbers)

#EX 2
#Given a tuple which value is integers, is it possible to add more integers to the tuple?
bag_of_rice = (10,25,40,67)
bag_of_rice1, bag_of_rice2, bag_of_rice3, bag_of_rice4 = bag_of_rice 
print(bag_of_rice1)
print(bag_of_rice2)
print(bag_of_rice3)

#if you want to change a tuple, you need to convert it to a list, add what you want then change it back to a tuple.
#convert tuple to list
bag_list = list(bag_of_rice)
bag_list.append(88)

#convert list back to tuple
updated_tuple = tuple(bag_list)
print(bag_list)

#EX 3
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")

print(basket)

#EX 4
# Recap – What is a float? What is the difference between an integer and a float? 
# MY ANSWER - a float is a number, positive or negative, containing one or more decimals, an integer is a whole number, positive or negative, without decimals, of unlimited length.. 

# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
import numpy #https://sparkbyexamples.com/python/python-range-with-float-values/#:~:text=As%20range()%20doesn't,the%20range%20of%20float%20values.
n = ()
for n in numpy.arange(1.5,5,.5): #Range indexes return a list from one index to the other (sequence_name[start:end]).
    print(n)

#the more correct way to do it for the level we are at right now:
sequence = []
for i in range(1,6):
    decimal = i +0.5
    sequence.append(i)
    sequence.append(decimal)
print(sequence[1:-1])

# Can you think of another way to generate a sequence of floats?
# MY ANSWER - 
import random
print(random.uniform(0,10))


#EX 5
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
for _ in range(0, 21):
    print(_)
for _ in range(0, 21, 2):
    print(_)

#EX 6
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
name = ['Mike']
Keep_Asking = True #this is a boolean flag. It was initiated in true so the program can ask.

while Keep_Asking:
    new_name = input("what is your name? ")
    if new_name == 'Mike':
        Keep_Asking = False
    else:
        Keep_Asking = True


#EX 7
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fav_fruit = input("what is your favorite fruit? Separate answers with a space eg. apple mango cherry: ")
fav_fruit_list = fav_fruit.split()

print('You like:', fav_fruit_list)

any_fruit = input("Now name any fruit: ")
if any_fruit in fav_fruit_list:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')

# # #EX 8
# # Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# # As they enter each topping, print a message saying you’ll add that topping to their pizza.
# # Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

Pizza_time = input('What would you like on your pizza? ' )
Pizza_time2_list = []
Total = 10
Pizza_time2_list.append(Pizza_time)
Keep_Asking = True
while Keep_Asking:
    Pizza_time2 = input('Topping added for $2.5, anything else? if not type Quit: ')
    Pizza_time2_list.append(Pizza_time2)
    Total += 2.5
    print(Pizza_time2_list)
    if Pizza_time2== 'Quit':
        Pizza_time2_list.pop()
        Keep_Asking = False

print(Pizza_time2_list)
print('Your total is',{Total})


#EX 9
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

family_cost = 0
Keep_Asking = True

while Keep_Asking:
    member = int(input('please provide the ages of your party, enter -1 to finish: ')) #because int the cost has to be +=  not append.
    if member == -1:
        Keep_Asking = False
    if member <=3: #under the age of 3
        family_cost += 0
    elif 3 < member <= 12: #between 3 and 12
        family_cost += 10
    elif 100 >= member >=12: #over the age of 12
        family_cost += 15

print('Your family total is',family_cost)

t_names = ['Brent','Piper', 'Brooklyn', 'Brice', 'Susan']
old_enough = [] #like the family members in the Loops_learning, it's an empty list because it needs to be added to.

for name in t_names:
    age = int(input(f'What is {name} age? '))
    if age <16 or age >21:
        old_enough.append(t_names)
    else:
        t_names.remove()
        print (f'{t_names} is not allowed in.' )
print(f'{t_names} is allowed.')

#EX 10
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []
while sandwich_orders:
    sandy = sandwich_orders.pop(0)
    finished_sandwiches.append(sandy)
    print(f"I made your {sandy}!")