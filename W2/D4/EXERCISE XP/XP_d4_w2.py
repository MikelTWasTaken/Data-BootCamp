# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.
# Hint : The generated sentences do not have to make sense.
# Download this word list DONE
# Save it in your development directory. DONE

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?
def get_words_from_file():
    with open('/Users/teitelbaumsair/Desktop/DI_Bootcamp/W2/D4/EXERCISE XP/sowpods.txt', 'r', encoding= 'utf-8') as f:
        wordys = f.readlines()
        return wordys
get_words_from_file()
# Create another function called get_random_sentence which takes a single parameter called length.
# The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.
# Take the random words and create a sentence (using a python method), the sentence should be lower case.
import random
def get_random_sen(len):
    wordys = list(get_words_from_file())
    phrase = random.sample(wordys, len)
    sentence = ' '.join(phrase).lower()
    x = sentence.replace("\n", " ")
    return x
print(get_random_sen(4))

# Create a function called main which will:
# Print a message explaining what the program does.
# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.
def main():
    print('The function calls in random words to create a sentence.' )
    try:
        testing = int(input('Request the length of your sentence: '))
        if testing <2 or testing >20:
            print("The length should be between 2 and 20.")
        else:
            print(get_random_sen(testing))
    except ValueError:
        print('The length has to be a number.')
main()

# 🌟 Exercise 2: Working with JSON
# Instructions
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)
salary = data['company'],['employee'],['payable'],['salary']
print(f'salary{salary}')
data["company"]["employee"]["birth_date"] = "1990-01-01"
with open('sampleJson.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("JSON file created with birth_date added.")
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.
