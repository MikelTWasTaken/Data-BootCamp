#LIST COMPREHENSIONS /SET COMPREHENSIONS/ DICTIONARY COMPREHENSION
#List, Set, dict

#quick ways for us to create instead of appending to lists.
#instead of:
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

#you can follow the below format:
# my_list = [param for param in itterable]
#OR
my_list= [char for char in 'hello'] #you create a list in your list that contains character in hello, you do a for loop and create a list.
print(my_list)
#for each variable in the itterable add it to the list.

my_list= [char for char in 'hello']
my_list2 = [num for num in range (0,100)] #for numbers as well

# #what if you want my_list2 to be multiplied by 2 or only odd, or only even?
# my_list3 = [num*2 for num in range (0,100)] #multiplies everything in the range by 2. But if you do to the power of 2, **2 you will get odd nbumbers. 
# my_list4 = [num**2 for num in range (0,100)if %2 == 0] #so what if you want only even numbers after **2? %2 == 0 #makes it even. if you wanted odd, you would do %2 != 0.
# print(my_list4)


some_list = ['a','b','c','b','d','m','n','n']
duplicates = [x for x in some_list if some_list.count(x)] #[x] represents the letters in the lsit. count tells us how many times an element appears in the list.
#the answer will give you ['b','b','n','n']
print(duplicates)

#so instead you can make it into a set without repeating elements. It would look like:
some_list = ['a','b','c','b','d','m','n','n']
duplicates = list(set([x for x in some_list if some_list.count(x)>1])) #we include >1 because we want the if function to check if our elements are greater than 1.
#but we also need to turn it back into a list. So we can create a list out of the set in the variable already.
print(duplicates)


#DICTIONARIES - DICT - a data type and a data structure, a way for us to organize data in a form that has pros and cons for accessing.
dictionary = {
    'a':1, #these are key value pairs, which are strings to grab the value. in order to access the value we would have to say dictionary and the key.
    'b':2
}
print(dictionary['b']) #i have this dictionary and I want to grab the value for 'b' which is the value 2. You can only look up key value pair defined in the dictionary.
#dictionaries are containers around data.

dictionary = {
    'a':[1,2,3],
    'b':'hello',
    'x': True
}
print(dictionary)
print(dictionary['a'][1])  #gives you the key list and the first indexed value in that list.

#you can also have multiple arrays in a dictionary.
dictionary = {
    'a':[1,2,3],
    'b':'hello',
    'x': True
}
my_list = [{
    'a':[1,2,3],
    'b':'hello',
    'x': True,
},
{
    'a':[4,5,6],
    'b':'hello',
    'x': True

}]
print(my_list[0], ['a'][2]) #prints 3,2

#DICTIONARY KEY EXPLANATION
dictionary = {
    123: [1,2,3],
    'greeting': 'hello',
    'is magic': True
}
print(dictionary[123]) #it gives you the set [1,2,3]
#dictionary keys need to be immuteable meaning they cannot change. It is usually something descriptive like a string.
#it also has to be unique. If there are same multiple keys they will overwrite.
#what if we don't know what is in a dictionary?
# 

user = {
    'basket': [1,2,3],
    'greeting': 'hello'
} 

print(user['age']) #it will give you an error because age is not a key in the dictionary. 
#in order to aboid this error, you can use .get on the object or dictionary. so the print will be:
print(user.get['age']) #if age doesnt exist then you can define it in the print statement like this:
print(user.get['age', 55]) #55 becomes a default value that says if there is no age, add age to the dictionary.

# user2 = dict(key=value) #the general format (not a common usage)
user2 = dict(name='mikemike')
print(user2)

#DICTIONARY METHODS
#looking for an item in a dictionary (like we've seen in lists by using the leyword 'in").

user = {
    'basket': [1,2,3],
    'greeting': 'hello'
} 

#you can check to see if something is in the dict.
print('basket' in user) #asks if basket exists in the variable user.
print('basket' in user.keys()) #checks the keys
print('hello' in user.values()) #checks the values
print(user.items())