# Class Decorators
# The decorators @classmethod, @staticmethod, and @property are used on functions defined within classes. They are built-in decorators.



# @staticmethod
# A static method is a method that doesn’t get self.

class MyClass:
  @staticmethod
  def add(a, b): 
    return a + b

print(MyClass.add(3, 6))
# >> 9


# The code belongs to a class but doesn’t use the object itself.
# It eases the readability of the code: when we use @staticmethod, we know that the method does not depend on the state of the object itself.
# It bounds a method to the class definition.


# Example:
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")
        
class Man(Person):
    sex = "Male"

    @staticmethod
    def get_nicknames():
        return ["Bro", "Dude", "Buddy"]

# Creating a Man instance
man = Man("John")

# Printing the name from the Man instance
man.greet()

# Printing the nicknames using the static method
print("Potential Nicknames:", ", ".join(Man.get_nicknames()))

# @classmethod
# Class methods are methods that are not bound to an object but to a class. Its first argument is the class itself (remember that classes are objects too).

class MyClass:
  __counter = 0

  @classmethod
  def add(cls,a): 
    return cls.__counter + a

my_class_add = MyClass.add(3)
print(my_class_add)
# >> 3

new_class = MyClass()
new_class.__counter = 1

print(new_class.add(3))
# >> 3

# The output is still three because the method add refers to the class definition, not the counter of the new_class instance


# @property
# 1. Getter
# Methods used in Object-Oriented Programming (OOPS) which helps to access the private attributes from a class.

# Without @property

class MyClass:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def email(self): 
    return f"{self.first_name}.{self.last_name}@gmail.com"

newClass = MyClass("John", "Doe")
print(newClass.email())
# >> John.Doe@gmail.com


# With @property

class MyClass:
  def __init__(self, first_name, last_name):
    self.__first_name = first_name
    self.__last_name = last_name

  @property
  def email(self): 
    return f"{self.__first_name}.{self.__last_name}@gmail.com"

newClass = MyClass("John", "Doe")

print(newClass.email())
# >> TypeError: 'str' object is not callable

print(newClass.email)
# >> John.Doe@gmail.com


# 2. Setter
# Methods used in Object-Oriented Programming feature which helps to set the value to private attributes in a class.

class MyClass:
  def __init__(self, first_name, last_name):
    self.__first_name = first_name
    self.__last_name = last_name

  @property
  def email(self): 
    return f"{self.__first_name}.{self.__last_name}@gmail.com"

  @email.setter
  def email(self, name): 
    self.__first_name = name

newClass = MyClass("John", "Doe")
newClass.email = "Sarah"
print(newClass.email)
# >> Sarah.Doe@gmail.com


# Example
class Person:

    used_names = set()

    def __init__(self, name, age):
        if name in self.used_names:
            name = input("That name is taken. Enter another name: ")

        self.name = name
        self.age = age
        self.used_names.add(name)

    @classmethod
    def fromYear(cls, name, birth_year):
        THIS_YEAR = 2020
        return cls(name, THIS_YEAR - birth_year)

    @property
    def professional_name(self):
        return "Mr " + self.name