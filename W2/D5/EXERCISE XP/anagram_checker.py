# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.

# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)

# Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.

# Note: None of the methods in the class should print anything.
import itertools

class Anagram_Checker:
    def __init__(self):
        with open('/Users/teitelbaumsair/Desktop/DI_Bootcamp/W2/D4/EXERCISE XP/sowpods.txt', 'r', encoding= 'utf-8') as f:
            open_file = f.read()
            self.words = open_file.split()

    def is_valid_word(self,word):
        if word.upper() in self.words:
            return True
        else:
            return False 

    def get_anagram(self,word): #user itertools permutations
        check = []
        anagram_list = []
        for anagram in itertools.permutations(word):
            check.append(''.join(anagram))
        for word in check:
            if self.is_valid_word(word) == False:
                continue
            else:
                anagram_list.append(word)
        print(anagram_list)
test = Anagram_Checker()

test.get_anagram('meat')
