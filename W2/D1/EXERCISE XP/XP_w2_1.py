
# 🌟 Exercise 1: Cats
# Instructions
# Using this class

# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age,cat_breed):
        self.name = cat_name
        self.age = cat_age
        self.breed = cat_breed

def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

first_cat = Cat('Boris', 8, "Maine Coon")
second_cat = Cat('Luna', 5, "Siamese")
third_cat = Cat('Whiskers', 10, "Persian")

cats = [first_cat, second_cat, third_cat]
oldest_cat = find_oldest_cat(cats)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
    



# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
class Dogs:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
        print(f'This is {dog_name} he jumps {dog_height} cm high')
    def bark(self):
        print(f'{self.name} goes woof')
        return f'{self.name} goes woof'
    def jump(self):
        print(f'{self.name} jumps {self.height} cm high!')
        return f'{self.name} jumps {self.height} cm high!'

Dog_1 = Dogs('Boris',69)
Dog_2 = Dogs('Luna', 20)

Dog_1.bark()
Dog_2.jump()

davids_dog = Dogs("Mushu", 50) #50CM 
print(davids_dog.bark)
print(davids_dog.jump)

sasha_dog = Dogs("Teacup", 20) #20CM 
print(davids_dog.bark)
print(davids_dog.jump)

biggest_dog = Dog_1  # Assume Dog_1 is the biggest initially
if Dog_2.height > biggest_dog.height:
    biggest_dog = Dog_2
if davids_dog.height > biggest_dog.height:
    biggest_dog = davids_dog
if sasha_dog.height > biggest_dog.height:
    biggest_dog = sasha_dog
print(f'The biggest dog is {biggest_dog.name}')

# 🌟 Exercise 3 : Who’s the song producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:  # Access self.lyrics directly, no need for extra parameters
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

new_animal = { 
    1: "Ape",
    2: ["Baboon", "Bear"],
    3: ['Cat', 'Cougar'],
    4: ['Eel', 'Emu']
}


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.animal_groups = {}
    def add_animals(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:", self.animals)

    def sell_animals(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        self.animals.sort()
        self.animal_groups = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.animal_groups:
                self.animal_groups[first_letter] = []
            self.animal_groups[first_letter].append(animal)

    def get_groups(self):
        print("Animal groups by first letter:")
        for letter, group in self.animal_groups.items():
            print(f"{letter}: {', '.join(group)}")



ramat_gan_safari = Zoo("Ramat Gan Safari")
# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

# Add animals to the zoo
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Elephant")

# Get the list of animals
ramat_gan_safari.get_animals()

# Sell an animal
ramat_gan_safari.sell_animal("Bear")
ramat_gan_safari.get_animals()  # Check that "Bear" was removed

# Sort animals and display groups
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()