#Lists and List Comprehension
# Example of list types
# li = [1,2,3,4,5]
# li2 = ['a', 'b', 'c']
# li3 = [1, 2, 'a', True]

#Lecture Examples
my_name = 'Mike'
l_name = 'Teitelbaum'
username = 'MT444'

#two options to create a list
user_info = [my_name, l_name, username] #wrap with square brackets []
user_info = list(my_name) #use built-in method list() automatically takes each character and makes it one element of the list. They also are given indexes in the list.

print(user_info)

amazon_cart = ['notebooks','sunglasses','diapers']
print(amazon_cart[0])

#list Slicing
#remember string slicing, you can also slice lists
string = "helloworld"
string [0:2:1]
# list slicing
amazon_cart = ['notebooks',
               'sunglasses',
               'diapers',
               'toys',
               'grapes'
]
print(amazon_cart[0::2]) #Start at 0(notebooks)and jump every two items
print(amazon_cart[0:4])

#if you want to change your cart you can because lists are muteable
amazon_cart[0] = 'laptop'
print(amazon_cart[1:3])
print(amazon_cart[0:3])
print(amazon_cart)

# So here we’re creating an entirely new list so that I could actually assign it to a variable new cart
# is going to be Amazon cart and let’s just do the same thing here and new cart is an entirely new list
# on its own. I could change a new cart let’s say zero into let’s say gum and if I print this you see that I have
# two new separate lists but a list is mutable because I can change whatever is at the index anytime I want.
# And every time we do list slicing we create a new copy of that list but I have a tricky question for
# you here what happens if I just do this if I run this.
# Did you see that instead of slicing my list I simply said that new cart is going to equal the Amazon
# cart and I changed a new cart index of 0 2 equal to gum but now my Amazon cart got modified as well.
# Why is that and this is a bit of a tricky question that you might encounter in an interview.
# The reason is that right now the way that I did equals means that hey new cart is going to equal Amazon
# cart.

# new_cart = amazon_cart[0] = 'laptop'
# new_cart[0] = 'gum'

#List Methods #1
basket = [1,2,3,4,5]
print(len(basket)) #If I calculate the length of the basket let’s do print here so we can see the result and I click Run 5 the length of the basket is five because while there’s five items remember a length is the actual length it doesn’t start counting from zero.

# #adding to the basket
print(basket.append(100))
# #or you can create a new list and add 100 to it.
new_list = basket.append(100)
# #OR
# new_list = basket.extend(100)
# print(new_list)


#----
#append vs.insert method
num_list = [1,2,3,4,5,6,10]
num_list.append(120)
print(num_list)

num_list.insert(2,55) #this puts 55 in the INDEX 2
print(num_list)

#removing
num_list.remove(2) #takes the ELEMENT out not the INDEX
print(num_list)

num_list.pop() #by default it will remove the last element
print(num_list)

num_list.pop(4) #If you want to know what was deleted you can save the pop as a variable
deleted_el = num_list.pop(4) #pop(index): delete the element in this index and save what was deleted.
print(num_list)
print(deleted_el)

print(num_list[2:])

#Modifying an element
print(num_list.index(4)) #If youre dealing with a massive data base you can index to find out what element is in index 4.
#index 4 is element 3 so...
num_list[3] = 40
print(num_list)

#---
#TUPLES: immutable sequences - cannot be changed.
#Two ways of mkaing tuples.
a_tuple = tuple()
my_tuple = (10,25,40,67)


#you can "unpack" a tuple by assigning variables to the elements in a tuple. 
#below we define scores, then name them score 1, score 2 etc. Then we can print the score assigned in the tuple. 
Scores = (10,25,40,67)
score1, score2, score3, score4 = Scores 
print(score1)
print(score2)
print(score3)

#if you want to change a tuple, you need to convert it to a list, add what you want then change it back to a tuple.
#convert tuple to list
score_list = list(Scores)
score_list.append(88)

#convert list back to tuple
updated_tuple = tuple(score_list)
print(score_list)

#LECTURE EXERCISE
#Given this list:
# list1 = [5, 10, 15, 20, 25, 50, 20]
# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
# Hint : Look at the index method
# Expected output:
# list1 = [5, 10, 15, 200, 25, 50, 20]

list1 = [5, 10, 15, 20, 25, 50, 20]
if list1.index(20):
    list1[list1.index(20)] = 200
print(list1)

#SETS: unordered and doesn't accept multiple occurances
# my_set = {} #comment out - to see the error AttributeError: 'dict' object has no attribute 'add' (because nothing was defined in the curly brackets).
# my_set = {''} #comment out - if you add '' it will say there is an empty set that can be filled.
my_set = set() #comment out - another method of writing a set.

my_set.add('rick')
my_set.add('morty')
my_set.add('rick')

print(my_set) #only two values will print
# print(my_set[0]) #an error will print because you cannot index a set.

set2 = {'Harry', 'Ron', 'Morty'}

set3 = my_set.intersection(set2)
print(set3)

set4 = my_set.union(set2)
print(set4)

#Converting a set to a list and then back to a set, and it doesnt keep the index of the list.
names = ['Stan', 'Jim', 'Roth', 'Dav', 'Dav']

names_set = set(names)
names.append('jerry') #this wont work becuase you can't add to a set.
print(names_set)

names = list(names_set)
names.append('stew') #make it a list to add a new name
print(names)

