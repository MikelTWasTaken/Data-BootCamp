#Write a program to reverse the sentence wordwise.

# Input:
# You have entered a wrong domain

# Output:
# domain wrong a entered have You

Reverse_inp= input("Enter a sentence: ")
words = Reverse_inp.split(" ")
reverse_words = words[::-1]
reversed_sentence = " ".join(reverse_words)
print(reversed_sentence) 