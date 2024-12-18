# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2 #diamerter is the radius times 2 

    def get_radius(self):
        return self.radius 
    def get_diameter(self):
        return self.diameter
    def get_area(self):
        PI = 3.142
        return PI *(self.radius ** 2) 
    def __str__(self):
        return f"Circle with radius {self.radius} and diameter {self.diameter}"
    
cr1 = Circle(5)
cr2 = Circle(10)


print(cr1) #Circle with radius 5 and diameter 10
print(cr2) #Circle with radius 10 and diameter 20

if cr1.get_area() > cr2.get_area():
    print("Circle 1 is bigger")
else:
    print("Circle 2 is bigger")