#learning for day 3

#map, filter, zip, and reduce
#MAP
# map (action, [1,2,3]) # The action can be multiplying, adding or any other definable action.

map(multiply_by2, [1,2,3]) #here the cation is defined as multiplying by 2 and the action will be on the int's 1,2,3
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
#The map needs to be below the function. Def has to be defined first. So it should look like this:

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(map(multiply_by2, [1,2,3])) 
#result is <map object at 0x100bfe230> it is not able and needs to be turned into a list in order to see the actual result.
#however, with map, you no longer need to turn something into a list with extra code. You only need something that returns (item*2) no append needed. 


def multiply_by2(item):
    return item*2
print(list(map(multiply_by2, [1,2,3])))
#Essentially map just takes the command in "return" and does the rest in print. Map calls the function and loops through all of the items that need an action taken on them.
#answer would be [2,4,6]

#Alternatively you can define a list
my_list = [1,2,3]
#run the same function
def multiply_by2(item):
    return item*2
print(list(map(multiply_by2, [1,2,3])))
#you can also print the original list and it wont be changed.
print(my_list)

#applicable to emails or usernames. You can itterate with the map function and change all the usernames in a list to capital letters.

#FILTER
my_list = [1,2,3]
def multiply_by2(item):
    return item*2

def check_odd(item): #here we want to filter out from our list to see if the numbers are odd.
    return item % 2 != 0 #means that the number is odd.
print(list(filter(check_odd, [1,2,3])))
#if you run it you remove the 2 becuase its even. We are not calling the function, becuase filter accepts a function signature(which memory space to access.

#ZIP WORKS LIKE A ZIPEPR. You need two lists or itterables and zips them together.

my_list = [1,2,3]
your_list = [10,20,30]
their_list = [5,30,12]
def multiply_by2(item):
    return item*2

def check_odd(item): 
    return item % 2 != 0 
#You can keep the previous functions in this and when you go to print just change the list method to zip.
print(list(zip(my_list,your_list))) #the two iterables my and your list and zips them together. (1,10),(2,20),(3,30)
#you can also do a list and a tuple together.

#REDUCE
#in order to use reduce:
from functools import reduce
my_list = [1,2,3]


def multiply_by2(item):
    return item*2

def check_odd(item): 
    return item % 2 != 0 
def accumulator(acc, item): #acc is the initial part of the function.
    print(0,1)
    return acc + item 
print(reduce(accumulator, my_list, 0)) #first we need the function, then we need the data.

#--------

#LIST UNPACKING
a,b,c = [1,2,3]

print(a)
print(b)
print(c)

#Gives you:
#1
#2
#3

#If we extended our list to 9 and just wanted to unpack 1,2,3 could we?
a,b,c *other, d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)
print (d) #gives you the last number in the list.

