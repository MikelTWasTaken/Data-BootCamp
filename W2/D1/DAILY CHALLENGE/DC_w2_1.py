# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output:
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.


# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheeps.”. The method should call the get_animal_types function to get a list of the animals.
# Note : In English the plural form of the word “sheep” is sheep. But for the purpose of the exercise, let’s say that if there is more than 1 animal, an “s” should be added at the end of the word.

class Farm: # Constructor method to initialize the farm's attributes
    def __init__(self, name):  # Method: Constructor
        # Attribute: Farm's name
        self.name = name
        # Attribute: Dictionary to hold animals and their counts
        self.animals = {}

    # Method to add animals to the farm
    def add_animal(self, animal, count=1):  # Method
        """
        Adds an animal to the farm. If the animal already exists, increments its count.
        """
        if animal in self.animals:
            # Increment the count if the animal is already present
            self.animals[animal] += count
        else:
            # Add a new animal with the given count
            self.animals[animal] = count

    # Method to get detailed information about the animals on the farm
    def get_info(self):  # Method
        """
        Returns a formatted string of all animals and their counts.
        """
        # Initialize the info string with the farm's name
        info = f"{self.name}'s farm\n"
        for animal, count in self.animals.items():
            # Append each animal and its count to the info string
            info += f"{animal} : {count}\n"
        # Add a final line and return the full info string
        info += "\n    E-I-E-I-0!\n"
        return info

    # Method to get a sorted list of animal types (names)
    def get_animal_types(self):  # Method
        """
        Returns a sorted list of animal types on the farm.
        """
        # Sort the animal names alphabetically
        return sorted(self.animals.keys())

    # Method to get a brief summary of the animals on the farm
    def get_short_info(self):  # Method
        """
        Returns a short summary of the farm's animals, using pluralization if needed.
        """
        # Get a sorted list of animal types and format them with pluralization
        animal_types = self.get_animal_types()
        animal_list = ', '.join(
            f"{animal}s" if self.animals[animal] > 1 else animal for animal in animal_types
        )
        # Return the formatted summary
        return f"{self.name}'s farm has {animal_list}."


# Example usage of the Farm class
macdonald = Farm("McDonald")  # Object instantiation
macdonald.add_animal('cow', 5)    # Adding animals using the add_animal method
macdonald.add_animal('sheep')      # Adding animals without specifying count (defaults to 1)
macdonald.add_animal('sheep')      # Adding another 'sheep' (should increase the count to 2)
macdonald.add_animal('goat', 12)   # Adding 'goat' with count 12

print(macdonald.get_info())        # Using the get_info method to print farm info
print(macdonald.get_animal_types())  # Using get_animal_types method
print(macdonald.get_short_info())    # Using get_short_info method