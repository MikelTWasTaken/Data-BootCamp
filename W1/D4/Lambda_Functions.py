# What you will learn:
# Lambda functions
# Map, Filter and Reduce paradigms


# Those functions allow you to apply a function across an iterable quickly. They all return a generator that can be converted to a list using the list built-in function.

# 1. The map() Function
# The map() function takes a function and a list (or any other iterable) and executes the function on every object of the list. It then returns the sequence containing all the results.

# For example:

# def upper_string(s):
#     return s.upper()

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(upper_string, fruit)

# print(list(map_object))
# >> ['APPLE', 'BANANA', 'PEAR', 'APRICOT', 'ORANGE']


# The returned map_object will contain every fruit in capital letters due to every fruit passed to the upper_string function.


# 2. The filter() function
# Similar to map(), filter() takes a function object and an iterable and creates a new list.

# As the name suggests, filter() forms a new list that contains only the elements that satisfy a particular condition, this condition is the function we passed as an argument, if it returns True, the element will be added to the new list, else it won’t.
# For example, the following snippet will return only the strings starting with an A.

# def starts_with_A(s):
#     return s[0] == "A"

# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# filtered_object = filter(starts_with_A, fruit)

# print(list(filtered_object))
# >> ['Apple', 'Apricot']


# 3. The functools.reduce() Function
# reduce() works differently than map() and filter(). It does not return a new list based on the function and iterable we’ve passed. Instead, it returns a single value.

# For example, the sum function is a reducing operation, it takes a list as an argument and returns a single number.

# A function passed to reduce needs to receive two arguments that will represent the first and the second element of the iterable, and then the second and the third, and then the third and the fourth, etc…

# For example, a snippet that recreates the sum function:

# from functools import reduce

# def sum_numbers(first, second):
#     return first+second

# my_list = [1, 3, 5, 7]
# reduced_list = reduce(sum_numbers, my_list)

# print(reduced_list)
# >> 16


# 4. Lambda functions
# Lambda functions are “one-line functions”, they only receive arguments and return a value, and they don’t need to be stored in variables (but they can !).

# Here is the syntax of a lambda function:

lambda arg1, arg2: value_returned
# For example, a function that returns a string in capital letters:

lambda s: s.upper()
# You can also store this function into a variable if you want to reuse it:

#syntax
my_function = lambda s: s.upper()
# This is the same as doing: 
def my_function(s):
    return s.upper()


# Those functions can be handy when using maps, filter, and reduce operations because they allow you to create it quickly. For example, let’s recreate the previous snippets using lambda functions.

# The map example:

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s.upper(), fruit)

print(list(map_object))


# The filter example:

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filtered_object = filter(lambda s: s[0] == "A", fruit)

print(list(filtered_object))


# The reduce example:

from functools import reduce
my_list = [1, 3, 5, 7]
reduced_list = reduce(lambda first, second: first+second, my_list)


# Exercise
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters

#check the length of each name
#if the name is <=4 then say "hello"

# Filter the names with length less than or equal to 4
filtered_names = filter(lambda name: len(name) <= 4, people)

# Map a "Hello" greeting to each name
greetings = map(lambda name: f"Hello, {name}!", filtered_names)

# Convert to list to see the results
print(list(greetings))

