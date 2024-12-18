# Challenge 1 : Sorting
# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
words = input("Enter a comma-separated sequence of words: ")
# rand_words = [input(word in word randword.split (word.join(',')) sorted.strip) ] #started with this as a concept.
sorted_words = ','.join(sorted([word.strip() for word in words.split(',')]))
print(sorted_words)


# Challenge 2 : Longest Word
# Instructions
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
# Examples

# longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

# longest_word("A thing of beauty is a joy forever.") ➞ "forever."

# longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"


def longest_word(statement):
    words = statement.split()
    most = max(words, key=len)
    return most

statement = input('please provide a sentence for analysis: ' )
print(longest_word(statement))