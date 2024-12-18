#Daily_Challenge_3

# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}
word_dict={} #create a dictionary
word = input('Enter word: ') #ask for a word

for i, char in enumerate(word): #you need to loop through the word and keep track of the index. 
    if char not in word_dict: #if the word is not inside you can add it to the dictionary
        word_dict[char] = [] #clarify the list to be added to
        word_dict[char].append(i) # Append the i to the list for this letter
    else:
         word_dict[char].append(i)     #if there are any repeating letters so it needs to be enumerated
print(word_dict)

# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

wallet = '$399'
check_items = {
    'laptop': '$500',
    'headphones': '$150',
    'keyboard': '$70',
    'monitor': '$300',
    'mouse': '$50'
}
wallet_amount = int(wallet.replace("$", ''))
affordable_items = []

for item in check_items:
    price = check_items[item]
    item_price = int(price.replace("$", ''))
    
    if item_price <= wallet_amount:
        affordable_items.append(item)

affordable_items.sort()

if affordable_items:
    print(affordable_items)
else:
    print("Nothing")
