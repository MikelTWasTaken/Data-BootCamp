# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

Car_comp = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
build_stats = Car_comp.split(',')
print(build_stats)

for name in build_stats:
    build_stats.sort()
print(build_stats)

build_stats_sum = len(build_stats)
print(f'There are {build_stats_sum} car companies in this list')

build_stats.sort()
if build_stats:
    print(build_stats)

build_stats_len = [word for word in build_stats if 'o' in word]  # Filter words with 'o'
print(f'There are {len(build_stats_len)} car companies with "O" in this list')

build_stats_len = [word for word in build_stats if 'i' not in word]  
print(f'There are {len(build_stats_len)} car companies without "I" in this list')