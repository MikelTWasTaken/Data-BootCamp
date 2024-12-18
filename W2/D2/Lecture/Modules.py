#Modules
# One advantage of functions is the way they separate blocks of code from your main program. By using descriptive names for your functions, your main program will be much easier to follow.

#An import statement tells Python to make the code in a module available in the currently running program file.

# Creating a module
# A module is just a python file (a file with the .py extension).

# Let’s create a file called pizza.py containing the function make_pizza().

def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    """    
    print(f"\n Making a {size}-inch pizza with the following toppings:")   
    for topping in toppings:        
        print(" - " + topping)


# We will create another file called making_pizzas.py (in the same directory as pizza.py).
# This file will import the function we just created and made two calls to it.

# Importing an Entire Module
# To import an entire module:

# use the import statement,
# followed by the name of the module (without the extension).
# For example, to import the pizza.py file:

import pizza # type: ignore


# When Python reads this file, import pizza tells Python to open the file pizza.py and copy all the functions from it into this program.

# You don’t see code being copied between files because Python copies the code behind the scenes as the program runs.

# All you need to know is that any function defined in pizza.py will now be available in making_pizzas.py.

# To call a function from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make_pizza(), separated by a dot.

import pizza # type: ignore

pizza.make_pizza(16, 'pepperoni') 
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Importing specific functions
# You can also import a specific function from a module. Here’s the general syntax for this approach:

# from module_name import function_name


# You can import as many functions as you want from a module by separating each function’s name with a comma:

# from module_name import function_0, function_1, function_2


# The making_pizzas.py example would look like this if we want to import just the function we’re going to use:

from pizza import make_pizza # type: ignore

make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using alias
# You can give a nickname to each module/function you import. This nickname, a short, unique alias (an alternate name similar to a nickname for the function), is defined as` keyword.

from pizza import make_pizza as mp # type: ignore


# The general syntax for a function is

from module_name import function_name as alias_name # type: ignore


# And for a module:

import module_name as alias_name # type: ignore


# Exercise
# Create a file called operators.py

# Create 2 functions : addOperator(x,y) that returns the addition of 2 numbers, and divideOperator(x,y) that returns the division of 2 numbers

# Create another file called calculator.py, and import the operators module. Call the 2 functions and display the results

# Do this process 3 times :

# once by importing the whole module
# the second time by importing specific functions
# the third time by using alias