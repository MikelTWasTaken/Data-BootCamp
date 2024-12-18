# Part 1 : Quizz :
# Answer the following questions

# What is a class?
    #ANSWER -  Data blueprint oriented to a single unit for creating objects.

# What is an instance?
    #ANSWER - An objcet that resides within the data blueprint (class)

# What is encapsulation?
    #ANSWER - Bundling the data (attributes) and methods (functions) that operate on the data into a single unit, or class. It also restricts access to certain components, protecting the internal state of an object from unintended interference.

# What is abstraction?
    #ANSWER - Focuses on hiding the complex implementation details of a system and exposing only the essential features.

# What is inheritance?
    #ANSWER - Inheritance allows a new class (subclass) to inherit properties and behaviors (methods and attributes) from an existing class (superclass or parent class).

# What is multiple inheritance?
    #ANSWER - Construct multiple objects from our class, we might want to set up different initial values for each of the objects

# What is polymorphism?
    #ANSWER - Allows objects of different classes to be treated as objects of a common superclass.

# What is method resolution order or MRO?
    #ANSWER - Order/ hierarchy through which a program is run. 



# Part 2: Create a deck of cards class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class DeckOfCards:
    def __init__(self):
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        if len(self.cards) != 52:
            raise ValueError("The deck must contain exactly 52 cards before shuffling.")
        
        random.shuffle(self.cards)

deck = DeckOfCards()
deck.shuffle()
print(deck.cards)