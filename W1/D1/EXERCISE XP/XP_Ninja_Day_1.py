# Exercise 1 : Use the terminal
# Instructions
# Run this command in the terminal to open a python console:
# $ python3
# Hint: Replace python3 with python for Windows

#DONE

# Read about the PATH variable. Try to explain why you can call python3 if you aren’t in the executable directory.
# PATH explanation can be found here.


# Exercise 2 : Alias
# Instructions
# Read about alias, and try to open a python console with the command:
# $ py

#DONE

# Exercise 3 : Outputs
# Instructions
# Predict the output of the following code snippets:
#     >>> 3 <= 3 < 9 - TRUE
#     >>> 3 == 3 == 3 - TRUE
#     >>> bool(0) - FALSE
#     >>> bool(5 == "5") - FALSE
#     >>> bool(4 == 4) == bool("4" == "4")-TRUE
#     >>> bool(bool(None)) - FALSE
#     x = (1 == True) - TRUE
#     y = (1 == False) - FALSE
#     a = True + 4 - (5)
#     b = False + 10 - (10)

#     print("x is", x) - TRUE
#     print("y is", y) - FALSE
#     print("a:", a) - 5
#     print("b:", b) - 10




# Exercise 4 : How many characters in a sentence ?
# Instructions
# Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

# Exercise 5: Longest word without a specific character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

longest_sentence = ""
while True:
    long_sentence = input("Please give a sentence without using an 'A': ")
    if 'A' in long_sentence.upper():  # Check if 'A' or 'a' is in the sentence
        print("Nope, it contains an 'A'. Try again!")
    else:
        if len(long_sentence) > len(longest_sentence):
            longest_sentence = long_sentence
            print("Congratulations, this is the longest sentence without an 'A'!")
    print("Current longest sentence:", longest_sentence)
    
