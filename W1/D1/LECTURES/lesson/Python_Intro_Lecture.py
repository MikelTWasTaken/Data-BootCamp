# 5+3
# print(5+3)

# #Basic Data Types
# my_name = "mike"
# print(type(my_name))

# my_bool = True
# print(type(my_bool))

# some_variable = 35
# print(type(some_variable))

# some_variable = 5.5
# print(type(some_variable))

# #STRINGS
# \n will jump a line
# \t will jump a space    
greeting = "shabbat shalom"

# #index a string
# print(greeting[3])
# print('index of space', greeting.index('s'))

# #Slice a String
print(greeting[2:4])
print(greeting[2:])

# #Len - String most used methods
# print(greeting[2:len(greeting)])
# print(len(greeting))

# #string methods
# print('shalom'.capitalize())
# print(greeting.title())
# print(greeting.replace('shalom', 'meburach').title())

# greeting_new = (greeting.replace('shalom', 'meburach').title())
# print((greeting_new))

# student = '   Harry Potter  '
# student = student.strip()
# print(student + " " + greeting_new)

# student.replace('r','')
# print(student.replace('r',''))

# #NUMBERS: integers, float, complex numbers, boolean
# my_num = 5
# float_num = 4.1

# #OPERATIONS
# print(type(float_num))
# print(-6 +3)
# print(10*2)
# print(5**2)

# print(greeting*10)

# print(round(5/3,4))
# #round will allow you to define how many decimal places you want.
# #Add a comma after the operation to define how many decimal places.
# # print(11//2)
# # print(11%2)

# # # if 12%3 == 0
# #     print('Yes!')

# my_age = 32
# print(my_age + 213879)

# my_age = str(my_age)
# print(type(my_age))

# my_phone = '0547464524'
# #my_phone = int(my_phone)
# print (my_phone)

# my_age = int(input('what is  my age?'))
# print(type(my_age))

# # if my_age < 18:
# #     print("You can't deink Vodka")
# # else:
# #     print("Bottoms up!")

# #COOMPARISON OPERATORS
# print (5<=7)

# #ADDING DATA TYPES
# f_name = 'Hermione'
# l_name = 'Grainger'
# hg_age = 15

# print("Hello," + f_name + ' ' + l_name +',welcome to Hogwarts')

# #f string
# print(f'Hello,{f_name} {l_name}, welcome to Hogwarts. Your age is {hg_age}')
# print(f'Your age is {hg_age}')

#exercise 2
# fn = 'Mike'
# ln = 'Teitelbaum'
# my_age
# print(f'{fn} {ln}')
# print("Hello, {}. You are {}.".format(fn +  ln ,my_age))

# print('python' is not 'python')
# print('python' is 'python')
# print('python' == 'python')
# print('python' != 'python')
# print('HTML' is not 'CSS' and 'Python' is 'Javascript')

# if 'HTML' is not 'CSS' and 'Python' is 'Javascript':
#     print ("That's Right!")
# else:
#     print("Wrong!")

# if 'HTML' is not 'CSS' and 'Python' is not 'Javascript':
#     print ("That's Right!")
# else:
#     print("Wrong!")

# my_age += 1
# print(my_age)

# my_age = input("How old are you? ")
# print(f"You are {my_age} years old")
# print(my_age > 18)