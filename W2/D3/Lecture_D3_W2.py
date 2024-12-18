# A Python module is a Python file containing a set of functions and variables to be used in an application. The variables can be of any type (arrays, dictionaries, objects, etc.)

# Modules can be either:

# Built in

# User-defined.

# 1) User-defined Modules
# Create a Module
# To create a module, create a Python file with a .py extension.

# Call a Module
# Modules created with a .py extension can be used in another Python source file, using the import statement.


# Here’s an example of a simple module, myModule.py:

#myModule.py
def myFunction( parameter ):  #define a function in myModule.py
   print "Course : ", parameter # type: ignore
   return
# To call this Python module myModule.py, create another Python file callModule.py file and use the import statement.

import myModule.py: # type: ignore
myModule.myFunction(“Python Programming”) # type: ignore
# When the Python interpreter encounters an import statement, it imports the module if it is present in the search path.

# A search path is a list of directories that the interpreter searches for importing a module.

# When the above code is executed, the following output is produced:

# callModule.py

#callModule.py
import myModule
myModule.myFunction("Python Programming")
myModule.py

#callModule.py
import myModule
myModule.myFunction("Python Programming")

# 2) Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

# Call a built-in Module
# To call a built-in Module and use the function of that module write:

import moduleName #call a module
moduleName.function()#use module function


import math
print("The value of cosine is", math.cos(3))
print("The value of sine is", math.sin(3))
print("The value of tangent is", math.tan(3))
print("The value of pi is", math.pi)


# Benefits of modules in Python
# There are a couple of key benefits of creating and using a module in Python:

# Structured Code
# Code is logically organized by being grouped into one Python file which makes development easier and less error-prone.
# Code is easier to understand and use.

# Reusability
# Functionality defined in a single module can be easily reused by other parts of the application. This eliminates the need to recreate duplicate code.

#Python collections module
# 1. Defaultdict
# Defaultdict is exactly like a dictionary in python. The only difference is that it does not give an exception/key error when you try to access the non-existent key.

# In the following code, even though the 4th index was not initialized, the compiler still returns a value, 0, when we try to access it.

# Example:

from collections import defaultdict  
nums = defaultdict(int)  
nums['one'] = 1  
nums['two'] = 2
nums['three'] = 3 
print(nums['four'])  

# 2. Counter
# Counter is a built-in data structure which is used to count the occurrence of each value present in an array or list.

# The following code is counting the number of occurrences of the value 2 in the given list.

# Example:

from collections import Counter  
list = [1,2,3,4,1,2,6,7,3,8,1,2,2]  
answer=Counter()
answer = Counter(list)  
print(answer[2]) # type: ignore