import random


class Deck:
    """
    A Deck that allows the director to draw a card with a different or random number from 1 to 13.

    The responsibility of a Deck is to draw a ranmdom card number from 1 to 13.
   
    Attributes:
        value (int): The number of the card drawn.
    """

    def __init__(self):
        """
        Constructs a new instance of Deck with a different or random number from 1 to 13.

        Args:
            self (Deck): An instance of Deck.
        """
        self.card_value = self.draw()

    
    def draw(self):
        """
        Generates a new random value.
        
        Args:
            self (Deck): An instance of Deck.
        """
        # Individual cards are represented as a number from 1 to 13.
        return random.randint(1, 13)