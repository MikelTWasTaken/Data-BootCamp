#Ex 1 
#Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
print('Hello World\t'*4)

#Ex 2
#Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
print((99**3)*8)

#Ex 3
# Predict the output of the following code snippets:
# >>> 5 < 3 FALSE
# >>> 3 == 3 TRUE
# >>> 3 == "3" TRUE
# >>> "3" > 3 FALSE
# >>> "Hello" == "hello" FALSE

# #Ex 4
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
computer_brand = 'MacbookAir_Pro'
print (f'I have a {computer_brand} computer')

# #Ex 5 Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code
name = 'Mike'
age = '32'
shoe_size = '45'
info = f'Hello, my name is {name}. I am {age} years old. My shoe size is {shoe_size}'

print(info)

# #Ex 6
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

a = 459
b = 19

if a>b:
    print ('Hello World!')

#Ex 7
# Write code that asks the user for a number and determines whether this number is odd or even.
num = int(input("Can you give me a number, and I'll tell you if its odd or even?"))
if (num %2 == 0):
    print ('Even')
else:
    print ('Odd')

#Ex 8
#Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
name = input("Dost thou have the same name as thyself?")
if name == "Mike":
    print ("Aye, 'tis the same name as mine own.")
else:
    print ("Nay, 'tis not the same name as mine own... Thou art an imposter!.")

# #Ex 9
# Write code that will ask the user for their height in centimeters.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

height = int(input("Hey you, with the legs... how tall arre you?"))
if height >= 145:
    print ('You are tall enough, enjoy the ride!')
else:
    print ('Not this year, little one. Maybe next year')