# Try to recreate the class explained below:

# We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

# We can create a class called BlockedDoor that inherits from the base class Door.

# We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor version of those functions, which simply raises an Error that a blocked door cannot be opened or closed.
#This is how the code works if we want to see it print an error:

################################################################################################

# Parent class - Door
# Parent class - Door
class Door:
    # Constructor method (initializer) for Door
    # Attribute: is_opened (used to store the door's state: open or closed)
    def __init__(self, is_opened):
        self.is_opened = is_opened  # Attribute of the Door class

    # Method to open the door
    def open_door(self):
        if not self.is_opened:
            print("The door is now open.")
            self.is_opened = True  # Modify the state to "open"
        else:
            print("The door is already open.")  # If already open, notify user

    # Method to close the door
    def close_door(self):
        if self.is_opened:
            print("The door is now closed.")
            self.is_opened = False  # Modify the state to "closed"
        else:
            print("The door is already closed.")  # If already closed, notify user


# Child class - BlockedDoor (inherits from Door)
class BlockedDoor(Door):
    # Overriding the open_door method of the parent (Door) class
    def open_door(self):
        # This line will raise an error because the door is blocked
        # raise Exception("This door is blocked and cannot be opened.")  # Error raising line
        print("This door is blocked and cannot be opened.")
    
    # Overriding the close_door method of the parent (Door) class
    def close_door(self):
        # This line will raise an error because the door is blocked
        # raise Exception("This door is blocked and cannot be closed.")  # Error raising line
        print("This door is blocked and cannot be closed.")


# -----------------------------------
# Testing the classes

# Creating an instance of the Door class (parent class)
door = Door(False)  # Door starts as closed (False)
door.open_door()    # Open the door
door.close_door()   # Close the door

# Creating an instance of the BlockedDoor class (child class, inheriting from Door)
blocked_door = BlockedDoor(False)  # BlockedDoor starts as closed (False)
blocked_door.open_door()  # Trying to open the blocked door
blocked_door.close_door()  # Trying to close the blocked door

# Key Changes:
# Error Handling: In the BlockedDoor class, the open_door and close_door methods now raise a ValueError instead of printing an error message directly. This is done as requested in the original prompt.

# Exception: The ValueError is raised with a message indicating that the door is blocked and cannot be opened or closed.

# Key Components Explained:
# Attributes:

# is_opened is an attribute of the Door class. It's used to track whether the door is open (True) or closed (False).
# Methods:

# open_door() and close_door() are methods of the Door class that modify the is_opened attribute and print messages about the door's state.
# In BlockedDoor, these methods are overridden to raise a ValueError instead of modifying the state of the door.
# Parent and Child Class:

# Door is the parent class, and BlockedDoor is the child class that inherits from Door. BlockedDoor overrides the open_door and close_door methods to raise exceptions, instead of allowing actions.
# Testing:
# The code first tests a regular Door object by opening and closing it.
# Then, it tests a BlockedDoor object. When trying to open or close the blocked door, it raises an error and prints the exception message.

################################################################################################

#This is how the Code looks if it works properly:

# Parent class - Door
class Door:
    # Constructor method (initializer) for Door
    # Attribute: is_opened (used to store the door's state: open or closed)
    def __init__(self, is_opened):
        self.is_opened = is_opened  # Attribute of the Door class

    # Method to open the door
    def open_door(self):
        # If the door is not already open, open it and update the attribute
        if not self.is_opened:
            print("The door is now open.")
            self.is_opened = True  # Modify the state to "open"
        else:
            print("The door is already open.")  # If already open, notify user

    # Method to close the door
    def close_door(self):
        # If the door is not already closed, close it and update the attribute
        if self.is_opened:
            print("The door is now closed.")
            self.is_opened = False  # Modify the state to "closed"
        else:
            print("The door is already closed.")  # If already closed, notify user


# Child class - BlockedDoor (inherits from Door)
class BlockedDoor(Door):
    # Overriding the open_door method of the parent (Door) class
    def open_door(self):
        # Raising an exception to block the action (can't open a blocked door)
        raise Exception("This door is blocked and cannot be opened.")
    
    # Overriding the close_door method of the parent (Door) class
    def close_door(self):
        # Raising an exception to block the action (can't close a blocked door)
        raise Exception("This door is blocked and cannot be closed.")


# -----------------------------------
# Testing the classes

# Creating an instance of the Door class (parent class)
door1 = Door(False)  # Door starts as closed (False)
door1.open_door()    # Open the door
door1.close_door()   # Close the door

# Creating an instance of the BlockedDoor class (child class, inheriting from Door)
blocked_door = BlockedDoor(False)  # BlockedDoor starts as closed (False)
try:
    blocked_door.open_door()  # Trying to open the blocked door
except Exception as e:
    print(e)  # This will print: "This door is blocked and cannot be opened."

try:
    blocked_door.close_door()  # Trying to close the blocked door
except Exception as e:
    print(e)  # This will print: "This door is blocked and cannot be closed."

#OR LIKE THIS:

# Parent class - Door
class Door:
    # Constructor method (initializer) for Door
    # Attribute: is_opened (used to store the door's state: open or closed)
    def __init__(self, is_opened):
        self.is_opened = is_opened  # Attribute of the Door class

    # Method to open the door
    def open_door(self):
        if not self.is_opened:
            print("The door is now open.")
            self.is_opened = True  # Modify the state to "open"
        else:
            print("The door is already open.")  # If already open, notify user

    # Method to close the door
    def close_door(self):
        if self.is_opened:
            print("The door is now closed.")
            self.is_opened = False  # Modify the state to "closed"
        else:
            print("The door is already closed.")  # If already closed, notify user


# Child class - BlockedDoor (inherits from Door)
class BlockedDoor(Door):
    # Overriding the open_door method of the parent (Door) class
    def open_door(self):
        # Raising an exception to block the action (can't open a blocked door)
        raise ValueError("This door is blocked and cannot be opened.")
    
    # Overriding the close_door method of the parent (Door) class
    def close_door(self):
        # Raising an exception to block the action (can't close a blocked door)
        raise ValueError("This door is blocked and cannot be closed.")


# -----------------------------------
# Testing the classes

# Creating an instance of the Door class (parent class)
door = Door(False)  # Door starts as closed (False)
door.open_door()    # Open the door
door.close_door()   # Close the door

# Creating an instance of the BlockedDoor class (child class, inheriting from Door)
blocked_door = BlockedDoor(False)  # BlockedDoor starts as closed (False)
try:
    blocked_door.open_door()  # Trying to open the blocked door
except ValueError as e:
    print(e)  # This will print: "This door is blocked and cannot be opened."

try:
    blocked_door.close_door()  # Trying to close the blocked door
except ValueError as e:
    print(e)  # This will print: "This door is blocked and cannot be closed."