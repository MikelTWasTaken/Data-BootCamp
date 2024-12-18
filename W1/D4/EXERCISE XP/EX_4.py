#EX1
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message(course, name):
    print(f'I am learning {course} at {name}.')
display_message('Python', 'Developers Institute')

#EX2
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.
def favorite_book(title):
    print(f'My Favorite book is{title}. ')
favorite_book('Alice in Wonderland')

#EX3
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.
def describe_city(city='Reykjavik', country='Iceland'):
    print(f'The {city} is located in {country}.')

describe_city('Tel aviv', 'Israel') # testing out the function for myself.

#EX4
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
import random
def num_comp(num1):
    num2 = random.randrange(1, 101)
    print(num2)
    if num1 != num2:
        return 'False'
    else:
        return 'True'

print(num_comp(50))

#EX5
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.
def make_shirt(text='I love Python', size='L'):
    print(f'Your shirt text is {text}, and the size of that text is {size}')

make_shirt('I love Python' ,'M')
make_shirt("MAGA", "L")

#Bonus - not complete
def make_shirt(**kwargs):
    key, value = kwargs.items()
    print(f'Your shirt text is {key[1]}, and the size of that text is {value[1]}') 

make_shirt(keys= "maga",values="Large")


#EX6
# Instructions
# Using this list of magician’s names
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.


def show_magicians(list):
    for x in list:
        print(x)
   
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
show_magicians(magician_names)

# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.

def the_great(names):
    for index,name in enumerate(names):
       names[index] =  "the great " + name

the_great(magician_names)

print(magician_names)    

#EX7
# Instructions
# 1.Create a function called get_random_temp().
#   This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#   Test your function to make sure it generates expected results.

from random import randint
def get_random_temp():
    temp_list= []
    for _ in range (-10,41):
        temp_list = randint (-10,41)
    return temp_list
print(get_random_temp())

# 2.Create a function called main().
#   Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#   Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

def main():
    temperature = get_random_temp()
    print(f'The temperature right now is {temperature} degrees Celsius.')

main()
# 3.Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
#   below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
#    between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
#   between 16 and 23
#   between 24 and 32
#   between 32 and 40
from random import randint

def get_random_temp():
    return randint(-10, 40)
print(f'The temperature right now is {temperature} degrees Celsius.')

def main():
    temperature = get_random_temp()
    if temperature <0:
        print(f'Brrr, thats freezing! Wear some extra layers today')
    elif temperature <= 16:
        print(f'Quite chilly! Dont forget your coat')
    elif temperature <= 24:
        print(f'Its heating up, break out the shorts!')
    elif temperature <= 32:
        print(f'Beach time, get your baathing suits on and hit the surf!')
    elif temperature <= 40:
        print(f'Bring napkins becuase youre gonna melt.')

main()

# 4.Change the get_random_temp() function:
#   Add a parameter to the function, named ‘season’.
#   Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
#   Now that we’ve changed get_random_temp(), let’s change the main() function:
#       Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
#       Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.
from random import randint

def get_seasonal_temp(weather):
    for season in weather:
        if season == 'winter':
            return randint (-10,16)
        elif season == 'Spring':
            return randint (0,24)
        elif season == 'Summer':
            return randint (24,40)
        elif season == 'Fall':
            return randint (10,24)

def main():
     seasonality = input('Please pick a season: ')
     temp = get_seasonal_temp(seasonality)
     for seasonality in temp():
        print(f'the weather right now is {temp} degrees celcius.')

main ()


# #EX8
# # Instructions
# # This project allows users to take a quiz to test their Star Wars knowledge.
# # The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# # Here is an array of dictionaries, containing those questions and answers

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

#i need to write a function to:
# 1. access the data in the dictionary, and pose each question in the key index of the dict to the user.
#   a. that answer has to be checked agains the answer in values index of the dict.
#   b. if the answer is correct, move onto the next question while counting the correct answers and incorrect answers.
#   c. display the qquestions he got wrong and Ask if he wants to continue and "learn the ways of the force". If yes
#   d. if the incorrect answers exceed 3 then prompt the user with "please play again" and start the loop over from the first question. 
#   e. if no, end the quiz and say "you have given in to the dark side".
#plan of attack:
#start by writing out the place to store the answers with a while loop
#write all the if statements:
#if an answer is the same as the value in the dict add a point to correct answer storage 
#if an answer is wrong, add a point to incorrect answer storage and add their answer to the list of user answers.
#if the incorrect asnwers points is 3 or more, say to the player they got too many wrong.
#if there are more than more than 3 correct answers, and the quiz finishes say "the force is with you" and give the number of correct and incorrect answers.

def start_SW_quiz():
    while True:
        correct_count = 0
        incorrect_count = 0
        wrong_answers = ()

        for item in data:
            padawan_answer = input(item["question"], " ")
            
            if padawan_answer == item["answer"]:
                correct_count += 1
            else:
                incorrect_count += 1
                wrong_answers.append(padawan_answer)

            if incorrect_count >= 3:
                print("Too many incorrect answers! You have gone to the dark side.")
                print(f"Incorrect Answers: {incorrect_count}, {wrong_answers}")
                break
            
        if incorrect_count <= 3:
            print("The Force Is With You!")
            print(f"Correct Answers: {correct_count}")
            print(f"Incorrect Answers: {incorrect_count}")
            break

start_SW_quiz()