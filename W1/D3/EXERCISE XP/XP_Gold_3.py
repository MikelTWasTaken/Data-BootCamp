# Exercise 1: Birthday Look-up
# Instructions
# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
# Ask the user to give you a person’s name and store the answer in a variable.
# Get the birthday of the name provided by the user.
# Print out the birthday with a nicely-formatted message.

birthdays = {
    'Mike': "1992/06/04",
    'Sharon': "1994/04/06",
    'Eliav': "2023/08/23",
    'Alice': "1985/12/01",
    'John': "1990/07/15"
}
print(birthdays)
print("Welcome! You can look up the birthdays of the people in the list!")
name = input("Please give the name of someone you want to look up: ")
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, I don't have the birthday for {name}.")


# Exercise 2: Birthdays Advanced
# Instructions
# Before asking the user to input a person’s name print out all of the names in the dictionary.
# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)
birthdays = {
    'Mike': "1992/06/04",
    'Sharon': "1994/04/06",
    'Eliav': "2023/08/23",
    'Alice': "1985/12/01",
    'John': "1990/07/15"
}
print(birthdays)
print("Welcome! You can look up the birthdays of the people in the list!")
name = input("Please give the name of someone you want to look up: ")
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we dont have the birthday information for {name}")

# Exercise 3: Add Your Own Birthday
# Instructions
# Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# Ask the user for a person’s name – store it in a variable.
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.

birthdays = {
    'Mike': "1992/06/04",
    'Sharon': "1994/04/06",
    'Eliav': "2023/08/23",
    'Alice': "1985/12/01",
    'John': "1990/07/15"
}
new_name = input('Please provide your name: ')
new_bd = input('and your birthday: ')
birthdays.update({new_name:new_bd})
print("\nUpdated Birthdays List:")
print(birthdays)
print("Welcome! You can look up the birthdays of the people in the list!")
name = input("Please give the name of someone you want to look up: ")
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we dont have the birthday information for {name}")

# Exercise 4: Fruit Shop
# Instructions
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
# Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
# write some code to calculate how much it would cost to buy everything in stock.
# items = {
#     "banana": {"price": 4 , "stock":10},
#     "apple": {"price": 2, "stock":5},
#     "orange": {"price": 1.5 , "stock":24},
#     "pear": {"price": 3 , "stock":1}
# }
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
for item, price in items.items():
    print(f"The price of {item} is {price} dollars.")

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total_cost = 0
for item, details in items.items():
    cost = details["price"] * details["stock"]
    total_cost += cost
    print(f"{item.capitalize()}: {details['stock']} in stock, unit price {details['price']} dollars.")

print(f"\nThe total cost to buy everything in stock is: {total_cost} dollars.")

