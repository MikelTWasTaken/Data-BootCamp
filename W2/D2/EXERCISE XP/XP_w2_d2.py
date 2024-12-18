# 🌟 Exercise 1 : Pets
# Instructions
# Using this code:

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

cat_list = []

cat_list.append(Bengal('Bengal', 4))
cat_list.append(Chartreux('Chartreux', 5))
cat_list.append(Siamese('Siamese', 1))

saras_pets = Pets(cat_list)

saras_pets.walk()

# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.


# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking.'

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f'{self.name} wins the fight against {other_dog.name}!'
        elif self_power < other_power:
            return f'{other_dog.name} wins the fight against {self.name}!'
        else:
            return f'The fight between {self.name} and {other_dog.name} is a tie!'

# Create 3 Dog instances
bruno = Dog('Bruno', 5, 30)
king = Dog('King', 3, 25)
queen = Dog('Queen', 4, 28)

# Demonstrate methods
print(bruno.bark())
print(f"{bruno.name}'s run speed is {bruno.run_speed()}")

# Test fights between dogs
print(bruno.fight(king))
print(bruno.fight(queen))
print(king.fight(queen))

# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

from Dog_File import Dog
import random  # For choosing random tricks

class Pet(Dog):
    def __init__ (self, name, age, weight, trained=False):
        super().__init__ (name, age, weight, trained)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.train = True

    def play(self, *other_dogs):
        dog_names = ', '.join(dog.name for dog in (self, *other_dogs))
        print(f"{dog_names} all play together.")
        return f'{self.name} is playing.'
    
    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained to do tricks yet.")

# Exercise 4 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries
# last_name : (string)

# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ details.

# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#     ]
class Family:
    def __init__(self,members,last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(**kwargs)
        print(f'{kwargs.get} {self.last_name} has been born.' )

    def is_18(self, name):
        for member in self.memebers:
            if member ['name'] == name:
                return member['age'] >= 18
        return None

    def family_presentation(self):
        print(f"Family Last Name: {self.last_name}")
        print("Family Members:")
        for member in self.members:
            print(f"  - Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")

initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

cohen_family = Family(members=initial_members, last_name="Cohen")

# Add a new family member using the born method
cohen_family.born(name='ELiav', age=0, gender='Male', is_child=True)

# Check if a member is over 18
print(cohen_family.is_18('Michael'))  
print(cohen_family.is_18('Emma'))  

cohen_family.family_presentation()

# Exercise 5 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)


# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# Add a method called incredible_presentation which :

# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)


# Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.

#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#     ]


# Call the incredible_presentation method.


# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


# Call the incredible_presentation method again.

import Family_time

class TheIncredibles(Family_time):
    def __init__(self,members,last_name):
        super().__init__ (members, last_name, )
        self.trained = trained # type: ignore
    def powers(self):
        for member in self.members:
            if member['name'] == name: # type: ignore
                if member['age'] >= 18:
                    print(f"{member['incredible_name']} uses their power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old and cannot use their power.")
                return
        print(f"No member with the name {name} found.") # type: ignore
    
    def family_presentation(self):
        print(f"Here is your super family!")
        super().family_presentation()
        for member in self.members:
            print(f"Incredible Name: {member['name']}, Age: {member['age']},  Power: {member['power']}")

initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredible_family = TheIncredibles(members=initial_members, last_name="Incredible")

# Call the incredible_presentation method
incredible_family.incredible_presentation()
incredible_family.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')
incredible_family.incredible_presentation()

try:
    incredible_family.use_power('Michael')  # Should work since Michael is over 18
    incredible_family.use_power('Jack')     # Should raise an exception since Jack is not over 18
except Exception as e:
    print(e)
