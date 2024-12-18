# Exercise 1 : Geometry
# Instructions
import math  # Import math module for pi

class Circle:
    def __init__(self, radius=1.0):  # Constructor with default radius
        self.radius = radius

    def perimeter(self):
        # Calculate the perimeter (circumference) of the circle
        return 2 * math.pi * self.radius

    def area(self):
        # Calculate the area of the circle
        return math.pi * (self.radius ** 2)

    def definition(self):
        # Print the geometrical definition of a circle
        print("A circle is a round shape with all points equidistant from its center.")

# Exercise 2 : Custom List Class
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).
import random

class My_list():
    def __init__(self, letters):
        self.letters = letters
    
    def reverse(self):
        return self.letters[::-1]

    def sorted(self):
        return sorted(self.letters)
    
    def generate_random_list(self):
        return [random.randint(1, 100) for _ in range(len(self.letters))]

letters = My_list(['b', 'a', 'd', 'c'])

print("Original list:", letters.letters)
print("Reversed list:", letters.reverse())
print("Sorted list:", letters.sorted())
print("Random list:", letters.generate_random_list())


# Exercise 3 : Restaurant Menu Manager
# Instructions
# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.

# Create a python file called menu_manager.py.

# Create a class called MenuManager.

# Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).

# Here is a list of the dishes currently on the menu:

#     Soup – 10 – B - False
#     Hamburger – 15 - A - True
#     Salad – 18 - A - False
#     French Fries – 5 - C - False
#     Beef bourguignon– 25 - B - True

#     Meaning: For the spice level:
#        • A = not spicy,
#        • B = a little spicy,
#        • C = very spicy


# The dishes provided above should be the value of the menu attribute.

# Create a method called add_item(name, price, spice, gluten)). 
# This method will add new dishes to the menu.

# Create a method called update_item(name, price, spice, gluten). 
# This method checks whether a dish is in the menu, if the dish exists then update it. 
# If not notify the manager that the dish is not in the menu.

# Create a method called remove_item(name). 
# This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.

class MenuManager:
    def __init__ (self): #__init__ Method: Sets up the initial menu with a list of dictionaries, each representing a dish.
        self.menu = [ #insert dictionary into menu
            {"name": "Soup", "price": 10, "spice_level": "B", "gluten_index": False},
            {"name": "Hamburger", "price": 15, "spice_level": "A", "gluten_index": True},
            {"name": "Salad", "price": 18, "spice_level": "A", "gluten_index": False},
            {"name": "French Fries", "price": 5, "spice_level": "C", "gluten_index": False},
            {"name": "Beef bourguignon", "price": 25, "spice_level": "B", "gluten_index": True}
        ]
    
    def add_item(self,name, price, spice_level, gluten_index): #add_item Method: Takes the dish details, creates a dictionary, and appends it to the menu.
        new_dish = {"name": name, "price": price, "spice_level": spice_level, "gluten_index": gluten_index}
        self.menu.append(new_dish)


    def update_item(self,name, price, spice_level, gluten_index):#update_item Method: Checks if a dish with the specified name exists. If found, updates the price, spice level, and gluten index; if not, prints a message.
        dish = {"name": name, "price": price, "spice_level": spice_level, "gluten_index": gluten_index}
        if dish in self.menu: #list what dish is equal to, and then if there is something that needs to be updated, then it will update the that specific detail for the dish. So if the spice level is lower, or there is no gluten when the boolean is true. 
            if dish["name"] == name:
                dish["price"] = price
                dish["spice_level"] = spice_level
                dish["gluten_index"] = gluten_index
                return
            print(f'the dish{name} has been updated.')

    def remove_item(self, name): #remove_item Method: Finds a dish by name and removes it from the menu if found; otherwise, prints a message.
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                return
            print(f'The dish {name} has been remove.')

menu_manager = MenuManager()
menu_manager.add_item("Pasta", 12, "A", False)          # Adding a new item
menu_manager.update_item("Soup", 12, "A", False)         # Updating an existing item
menu_manager.remove_item("Hamburger")                    # Removing an item
print(menu_manager.menu)                                 