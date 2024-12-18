class Dog():
    def __init__(self, name, color, age):
        self.name = name  # Assign name to the instance
        self.color = color  # Assign color to the instance
        self.age = age  # Assign age to the instance

    def bark(self):
        print(f'{self.name} is barking')
        return f'{self.name} is barking'
    def walk(self,num_meters):
        print(f'{self.name} walked {num_meters} meters')
        return f'{self.name} walked {num_meters} meters'

# Create instances of the Dog class
Shelter_dog = Dog('rex', 'black', 7)
Poodle = Dog('fluffy', 'white', 3)

# Call the bark method on each instance
Shelter_dog.bark()
Poodle.bark()

Shelter_dog.walk(3000)
Poodle.walk(3000)

Dog.bark(Shelter_dog)

