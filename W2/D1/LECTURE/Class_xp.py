#create a class called person
#use _init_() to create the following attributes: name, age, height
#create an object of this class for yourself (with the same attributes)
#print all attributes

class Person():
    def __init__(self, name, age, height):
        print("A new person has been initialized !")
        self.name = name
        self.age = age
        self.height = height
        print(self.name, self.age, self.height)  # Accessing the instance attributes

    def intro(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')  # Use self here
    
    def kids(self,num_kids):
        print(f'{self.name} has {num_kids} child.')
        

# Create an instance of Person
Me = Person('Mike', 32, 190)

# List of methods for the Instance withing the objcet.
Me.intro()
Me.kids(1) #define the number of kids in the instance. 