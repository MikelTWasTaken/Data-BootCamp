#  Exercise 1 : Convert lists into dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(list(zip(keys,values)))


# Exercise 2 : Cinemax #2
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Given the following object:
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# How much does each family member have to pay ? RESEARCHING
# Print out the family’s total cost for the movies. DONE
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

total_cost = 0
member_ind_cost = {}

for member, age in family.items():
    if age <= 3:
        cost = 0
    elif 3 < age <= 12:
        cost = 10
    else:
        cost = 15

    member_ind_cost[member] = cost
    total_cost += cost

print("Total Cost:", total_cost)
print("Individual Costs:", member_ind_cost)

#Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.

brand = {
    'name':'Zara',
    'Creation_Date': 1975,
    'Creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_compet': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue', 
        'Spain': 'red',
        'US': ['pink, green']
        }
}

# 3. Change the number of stores to 2.
brand['number_stores'] = 2
print(brand)

# 4. Print a sentence that explains who Zaras clients are.
x = brand.get('type_of_clothes')
print(f"Zara's clientelle purchase products from verticals such as: ",x)

# 5. Add a key called country_creation with a value of Spain.
brand.update({"country_creation": "Spain"})
print(brand)

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
brand_list = {'international_compet':['Gap', 'H&M', 'Benetton']}
brand_list['international_compet'].append('Desigual')
print(brand_list)

# 7. Delete the information about the date of creation.
brand.pop("Creation_Date")
print(brand)

# 8. Print the last international competitor.
x = brand['international_compet'][-1]
print(x)

# 9. Print the major clothes colors in the US.
x = brand['major_color']['US']
print(x)

# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))

# 11. Print the keys of the dictionary.
x= brand.keys()
print(x)

# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10000

more_on_zara = {
     'creation_date': 1975, 
     'number_stores': 10000
}
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

Final_Zara = brand.copy()
Final_Zara.update(more_on_zara)

print(Final_Zara)

# 14. Print the value of the key number_stores. What just happened ?
Final_Zara['number_stores']
print(Final_Zara)
#ANSWER - Only one 'number_stores' was printed becuase dictionaries must have unique values.If there are same multiple keys the last will overwrite.

# Exercise 4 : Disney characters
# Instructions
# Use this list :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

#personal notes:
#FOR INNUMERATE - loop prints the index and the value - from online learning
#0 Alex
#1 Steve
#2 Sara
#3 Dave
#for i, each_student in enumerate(students):
    # print(i,each_student)
# # Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
users = ["Mickey","Minnie","Donald","Ariel","Pluto"] #the list is defined, and it needs to become a dictionary. So use list comprehension to define what is in the dictionary.
disney_users_A = {users: i for i, users in enumerate(users)} 
print(disney_users_A)

# # Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers. # same for 1 applies to 2
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_B = {users: i for i, users in enumerate(users, start=1)}
print(disney_users_B)

# # Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_C = {users: i for i, users in enumerate(sorted(users))}
print((disney_users_C))

# # Only recreate the 1st result for:
# # The characters, which names contain the letter “i”.
new_dict = {}
for i in disney_users_A.items():
        print(i[0])
        if "i" in i[0]:
            new_dict[i[0]] = i[1]
print(new_dict)

# # The characters, which names start with the letter “m” or “p”.
new_dict = {}
for i in disney_users_A.items():
        print(i[0])
        if "m" in i[0]:
            new_dict[i[0]] = i[1]
        elif "p" in i[0]:
            new_dict[i[0]] = i[1]
print(new_dict)
