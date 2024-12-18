#https://octopus.developers.institute/courses/collection/93/course/258/section/55/chapter/267#
# Exercise 1 : What’s your name ?
# Instructions
# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.



# Exercise 2 : From English to Morse
# Instructions
# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.


# Exercise 3 : Box of stars
# Instructions
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:
# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************


# Exercise 4 : What is the purpose of this code?
# Analyse this code before executing it. What is the purpose of this code?
# def insertion_sort(alist):
#    for index in range(1,len(alist)):

#      currentvalue = alist[index]
#      position = index

#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1

#      alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)
