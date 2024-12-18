class Circle:
    color = "red"

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
       return Circle.color

circle1 = Circle(2)
circle1.color = 'blue'
print(circle1.color)
print(Circle.color)
print(circle1.get_color())
circle1.grow(3)
c2 = Circle(4)
print(circle1.diameter)
print(c2.diameter)

#change the color to blue
#create a second object circle 2 and check to see if the color was changed to blu or red