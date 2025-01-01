#https://octopus.developers.institute/courses/collection/93/course/258/section/56/chapter/279

# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.


# Starter code
# Here is a piece of code that will give you a random word.

import random

words = ['correction', 'childish', 'beach', 'python', 'assertive', 
         'interference', 'complete', 'share', 'credit card', 'rush', 'south']

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

def display_man(wrong_guesses):
    print("*****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*****************")

def display_hint(hint):
    print(" ".join(hint))

def main():
    answer = random.choice(words)
    hint = ["_" for _ in range(len(answer))]
    wrong_guesses = 0
    guessed_letters = []
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
        else:
            guessed_letters.append(guess)
            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1
                if wrong_guesses == 6:
                    display_man(wrong_guesses)
                    print("You lost!")
                    print("The answer was: " + answer)
                    is_running = False
            if "_" not in hint:
                print("You won!")
                print("The answer was: " + answer)
                is_running = False

if __name__ == "__main__":
    main()