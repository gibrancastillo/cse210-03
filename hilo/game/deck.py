import random

class Deck:
    """
    A deck that shuffles two cars  individual card with a different or random number from 1 to 13.

    The responsibility of a Deck is to shuffle the  card drawn.
   
    Attributes:
        value (int): The number of the card drawn.
    """

    def __init__(self):
        """
        Constructs a new instance of Card with a value.

        Args:
            self (Card): An instance of Card.
        """
        self.drawn()
    

    def shuffle(self):
        self.previous_card = self.drawn()
        self.current_card = self.drawn()


    def drawn(self):
        """
        Generates a new random value.
        
        Args:
            self (Card): An instance of Card.
        """
        # Individual cards are represented as a number from 1 to 13.
        return random.randint(1, 13)