# Instructions :
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.


# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.

# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
# Implement a classmethod that returns a Text instance but with a text file:
#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.
# Now, use the provided the_stranger.txt file and try using the class you created above.

from collections import Counter
class T_Analysis:
    def __init__(self, words):
        self.words = words.lower()
        self.word_list = self.words.split(" ")

    def word_frequency(self,recurring_word):
        recurring_word = recurring_word.lower()
        frequency = self.word_list.count(recurring_word)
        if frequency > 0:
            return f"The word '{recurring_word}' appears {frequency} times."
        else:
            return f"The word '{recurring_word}' is not in the text." 
        
    def most_common_word(self):
        word_counts = Counter(self.word_list)
        max_frequency = max(word_counts.values())
        most_common_words = [word for word, count in word_counts.items() if count == max_frequency]
        return f"The most common words are {', '.join(most_common_words)} with {max_frequency} occurrences."

    def unique_words(self):
        unique_words_set = set(self.word_list)
        return list(unique_words_set)  

    @classmethod
    def from_file(cls):
        with open('W2/D4/DAILY CHALLENGE/the_stranger.txt', 'r', encoding= 'utf-8') as f:
            book = f.read()
            return cls(book)

Text1 = T_Analysis('A good book would sometimes cost as much as a good house.')
book1 = T_Analysis.from_file()


print(Text1.word_frequency('good'))        
print(Text1.most_common_word())            
print(Text1.unique_words()) 
print(book1.word_frequency('name'))
