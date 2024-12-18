class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")


# What is a class? A class is like a blueprint. Imagine you have a toy factory. 
#   You can create lots of toys from the same blueprint. Each toy might have different colors or names, 
#    but they are all made from the same blueprint. In your case, the blueprint is called Computer. 
#    The factory makes computers from this blueprint!

# What does the description function do? 
#   The description function is like a computer telling you its name. 
#   It says, "Hi, I'm a computer, my name is..." and then it says the name you give it.

# What is self? 
#   self is like saying "me" when you're talking about yourself. 
#   So, when the computer talks to itself, it says "I am this computer," that's self. 
#   It's just a way for the computer to know which one it is when you have more than one.

# Why do we use mac_computer = Computer() and dell_computer = Computer()? 
#   These lines create two different computers! 
#   One is named mac_computer and the other is dell_computer. 
#   Each one is a separate computer made from the same blueprint.

# What happens when we say mac_computer.brand = "Apple"?
#   Here, we're giving the mac_computer a brand name! 
#   It's like giving your toy a sticker that says "Apple." 
#   But remember, only mac_computer gets the sticker; the other computer doesn't have it unless you give it one too.

# What happens with Computer.description(dell_computer, "Mark")?
#   Normally, you can call a function using a computer like this: dell_computer.description("Mark"). 
#   But here, we're using the blueprint itself (Computer) to tell the computer to describe itself. 
#   This is just another way to call the same function!

# Why are these two lines the same?

# Computer.description(dell_computer, "Mark")
# dell_computer.description("Mark")

# Both do the same thing because when you say dell_computer.description("Mark"), it is like telling dell_computer directly, "Tell me your name." But when you say Computer.description(dell_computer, "Mark"), you’re using the blueprint (the class) to tell the computer to describe itself.

