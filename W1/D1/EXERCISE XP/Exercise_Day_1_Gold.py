#EX1
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python
print(' Hello World' *4, ' I love Python' *4)

#EX2
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

month = int(input('Which month is it?'))
spring = 3,4,5
summer = 6,7,8
autumn = 9,10,11
winter = 12,1,2

if month in spring:
    print ("spring")
elif month in summer:
    print ("summer")
elif month in autumn:
    print ("autumn")
elif month in winter:
    print ("winter")

