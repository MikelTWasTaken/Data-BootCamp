# # #inheritance

# class Animal():
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} barked, WAF !")
# #Inheritance is when a class uses code constructed within another class. 
# #   Classes called child classes or subclasses inherit methods and variables from parent classes or base classes.

# rex= Dog("dog", 4, "wouaf")
# print('This animal is a:', rex.type)
# # >> This animal is a dog

# print('This dog has', rex.number_legs , ' legs')
# # >> This dog has 4 legs

# print('This dog makes the sound ', rex.sound)
# # >> This dog makes the sound wouaf

# rex.make_sound()
# # >> I am an animal, and I love saying wouaf

# class Dog(Animal):
#     def fetch_ball(self):
#         print("I am a dog, and I love fetching balls")

# rex = Dog('dog', 4, "Wouaf")
# print('This animal is a:', rex.type)
# # >> This animal is a dog

# rex.fetch_ball()
# # >> I am a dog, and I love fetching balls

# roger = Animal('Roger', 4, "Grr")
# roger.fetch_ball()
# # >> AttributeError: 'Animal' object has no attribute 'fetch_ball'

#THIS IS HOW THE CODE SHOULD LOOK AFTER SEEING ALL ITS PARTS SEPARATED OUT:
class Animal():  # Class Definition (Animal class)
    def __init__(self, name, number_legs, sound):  # Method (Constructor)
        self.name = name  # Attribute (name)
        self.number_legs = number_legs  # Attribute (number_legs)
        self.sound = sound  # Attribute (sound)
        self.type = self.__class__.__name__.lower()  # Attribute (type)
    
    def make_sound(self):  # Method (make_sound)
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):  # Inheritance (Dog class inherits from Animal)
    def __init__(self, name, number_legs, sound):  # Method (Constructor in Dog)
        super().__init__(name, number_legs, sound)  # Method (Calling superclass constructor)

    def bark(self):  # Method (bark)
        print(f"{self.name} barked, WAF !")

    def fetch_ball(self):  # Method (fetch_ball)
        print("I am a dog, and I love fetching balls")

class Puppy(Dog):  # Inheritance (Puppy class inherits from Dog)
    def __init__(self, name, number_legs, sound, age):  # Method (Constructor in Puppy)
        super().__init__(name, number_legs, sound)  # Method (Calling superclass constructor)
        self.age = age  # Attribute (age)

    def play(self):  # Method (play)
        print(f"{self.name} is playing around!")

rex = Dog("rex", 4, "Wouaf")  # Object Instantiation (rex is an instance of Dog)
puppy = Puppy("Buddy", 4, "Woof", 1)  # Object Instantiation (Buddy is an instance of Puppy)

# rex has a puppy
rex.puppy = puppy  # Adding puppy as an attribute to rex

# Now, let's print details
print('This animal is a:', rex.type)  # Attribute (type) of rex
print('This dog has', rex.number_legs, 'legs')  # Attribute (number_legs) of rex
print('This dog makes the sound', rex.sound)  # Attribute (sound) of rex

rex.make_sound()  # Method (make_sound) of rex
rex.bark()  # Method (bark) of rex
rex.fetch_ball()  # Method (fetch_ball) of rex

print('\nThis dog has a puppy named:', rex.puppy.name)  # rex's puppy's name
print(f"{rex.puppy.name} is {rex.puppy.age} years old.")  # rex's puppy's age

rex.puppy.make_sound()  # Method (make_sound) of puppy
rex.puppy.bark()  # Method (bark) of puppy
rex.puppy.fetch_ball()  # Method (fetch_ball) of puppy
rex.puppy.play()  # Method (play) of puppy

roger = Animal('Roger', 4, "Grr")  # Object Instantiation (roger is an instance of Animal)
roger.make_sound()  # Method (make_sound) of roger

# Class Definitions:

# class Animal(): This defines a class called Animal, which is a template for creating Animal objects.
# class Dog(Animal): This defines a class called Dog that inherits from Animal, meaning it inherits the attributes and methods of the Animal class.
# Methods:

# __init__(self, name, number_legs, sound): This is a constructor method that initializes the object's attributes when an instance of the class is created.
# make_sound(self): This is a method that prints a sound-related message using the sound attribute.
# bark(self): This method is specific to Dog objects and prints a message related to barking.
# fetch_ball(self): This method is also specific to Dog objects and prints a message related to fetching a ball.
# Attributes:

# self.name: This is an attribute of the Animal class, holding the name of the animal.
# self.number_legs: This is an attribute of the Animal class, holding the number of legs of the animal.
# self.sound: This is an attribute of the Animal class, holding the sound the animal makes.
# self.type: This is an attribute that dynamically stores the class name in lowercase (i.e., "animal" or "dog").
# Inheritance:

# The Dog class inherits from the Animal class, meaning it gets all of the attributes and methods from Animal unless they are specifically overridden in Dog.
# Object Instantiations:

# rex = Dog("rex", 4, "Wouaf"): This creates an instance of the Dog class, which automatically calls the __init__ method of Dog and initializes rex with the given parameters.
# roger = Animal('Roger', 4, "Grr"): This creates an instance of the Animal class, calling the __init__ method of Animal to initialize roger.

# II . Overriding Parent Methods
# When you create the same method inside the child class, you override the parent class method.
# It’s important to note that child classes override or extend the functionality of parent classes. The child class will have all the parent class’s functions, plus his functions.

# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

#     def make_sound(self):
#         print(f"I am an animal, and I love saying {self.sound}")

# class Dog(Animal):
#     def fetch_ball(self):
#         print("I am a dog, and I love fetching balls")

#     def make_sound(self):
#         print("I am an DOGGG !!! WOUAFFF!!")

# rex = Dog('dog', 4, "Wouaf")
# rex.make_sound()
# >> I am an DOGGG !!! WOUAFFF!!

# Breakdown:
# Class Definitions:

# class Animal: This defines the base class Animal, which has a constructor and a method (make_sound).
# class Dog(Animal): This defines the Dog class, which inherits from Animal. The Dog class can use the methods of Animal and adds its own methods like bark and fetch_ball.
# class Puppy(Dog): This defines the Puppy class, which inherits from Dog (and indirectly from Animal). It can use all methods from Dog (including the overridden grow method) and add new methods like play.
# Method Overriding:

# In Dog: The __init__ method in Dog overrides the __init__ method in Animal. This is done by calling super().__init__(name, number_legs, sound), ensuring that the Animal constructor is executed first.
# In Puppy: The __init__ method in Puppy overrides the __init__ method in Dog. It calls super().__init__(name, number_legs, sound), which ensures that the Dog constructor is called first, initializing all necessary attributes inherited from Dog.
# Methods:

# make_sound(self): This is a method in the Animal class that prints the sound the animal makes. It is inherited by both Dog and Puppy.
# bark(self): This is a method in the Dog class that prints the sound a dog makes. It is not overridden, so the method is directly available for Dog and Puppy.
# fetch_ball(self): This is another method in Dog that prints a message about the dog fetching a ball. It is also inherited by Puppy.
# play(self): This is a new method introduced in Puppy. It is not overriding any method; it's a new behavior for puppies.
# Overriding is happening in the __init__ methods of Dog and Puppy.
# Attributes:

# self.name, self.number_legs, self.sound, and self.type: These are attributes of the Animal class, initialized in its constructor and inherited by the Dog and Puppy classes.
# self.age: This is a new attribute introduced in Puppy.
# Summary of Method Overriding:
# The __init__ method is overridden first in the Dog class (replaces the __init__ of Animal) and then in the Puppy class (replaces the __init__ of Dog).
# The grow method (from the original question) would be a good example of method overriding if included. Similarly, the make_sound, bark, and fetch_ball methods can be inherited without overriding, while play is new to Puppy.