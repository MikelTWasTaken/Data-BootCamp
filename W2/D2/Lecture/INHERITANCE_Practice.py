# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color = "blue"

# nc = NewCircle
# print(nc.color)

######

#Comment Out Above ################################################################################################

######

class Circle:  # Class Definition (Circle class)
    def __init__(self, diameter):  # Method (Constructor)
        self.diameter = diameter  # Attribute (diameter)

    def grow(self, factor=2):  # Method (grow)
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor  # Attribute (updated diameter)

class NewCircle(Circle):  # Inheritance (NewCircle class inherits from Circle)
    def grow(self, factor=2):  # Method (grow)
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)  # Attribute (updated diameter)

nc = NewCircle(1)  # Object Instantiation (nc is an instance of NewCircle)
print(nc.diameter)  # Prints the initial diameter of nc

nc.grow()  # Method (grow) of nc
print(nc.diameter)  # Prints the updated diameter of nc

nc.diameter= (4)
print(nc.diameter)

#EXPLANATION:

# Functionality of the Code:
# Initially, the object nc is created with a diameter of 1 by calling NewCircle(1). The constructor of Circle is called via inheritance, and nc.diameter is set to 1.
# The first print(nc.diameter) outputs the initial diameter of nc, which is 1.
# When nc.grow() is called, the grow method of NewCircle is executed (since it's overridden in NewCircle). This method multiplies the diameter by the factor (default is 2) and then further multiplies the result by 2, effectively multiplying the diameter by 4.
# The second print(nc.diameter) outputs the updated diameter of nc, which is now 4 (1 * 2 * 2).

#DEEPER EXPLANATION:
# Class Definitions:

# class Circle: This defines a class Circle that represents a circle with a given diameter.
# class NewCircle(Circle): This defines a class NewCircle that inherits from the Circle class, meaning it inherits the methods and attributes from the Circle class but can also override or extend them.
# Methods:

# __init__(self, diameter): This is the constructor method of the Circle class. It initializes an instance of Circle with a given diameter. The self.diameter is set to the provided diameter.
# grow(self, factor=2): This is a method in the Circle class that modifies the circle's diameter by multiplying it by a factor. The default factor is 2, meaning the diameter will double if no factor is passed.
# grow(self, factor=2): This method in the NewCircle class overrides the grow method from Circle. It increases the diameter by a factor, but it multiplies the result by 2, which changes how the diameter is modified. This method is specific to NewCircle.
# Attributes:

# self.diameter: This is an attribute of both Circle and NewCircle classes, which holds the diameter value of the circle. It is modified within the grow method.
# Inheritance:

# NewCircle(Circle): The NewCircle class inherits from the Circle class, meaning it gets the __init__ method and the grow method of Circle unless overridden (which happens in the NewCircle class).
# The grow method is overridden in NewCircle to adjust the diameter differently, making the NewCircle class behave differently when its grow method is called.
# Object Instantiation:

# nc = NewCircle(1): This creates an instance of NewCircle with a diameter of 1. The __init__ method of Circle is called (because NewCircle inherits from Circle), setting nc.diameter to 1.

