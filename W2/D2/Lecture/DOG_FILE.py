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