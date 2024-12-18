#Comprehensions
#this is th most basic form of a list comprehension in a for statement.
#I want 'n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

#instead you can write it like this:
my_lsit = [n for n in nums]
print(my_lsit)


#Example2:
#I want 'n**n' for each 'n' in nums.
#most basic form of writing it out
my_lsit = []
for n in nums:
    my_lsit.append(n**n)
print(my_lsit)

#Example 3:
#instead, you can write it like this:
my_lsit = [n**n for n in nums]
print(my_lsit)

#Example 4:
#I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)

#using list comprehension:
my_list = [n for n in nums if n%2 ==0]

