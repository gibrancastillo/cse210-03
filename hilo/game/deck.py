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
    
    def next_drawn(self,the_card_value):
        """
        This function takes in the previous card value and generates a new one without considering the previous
        
        Args:
            self for instantiation
            the_card_value:for exclusion of previously picked card
        """
        card_range = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        for i in card_range:
            if i == the_card_value:
                card_range.pop(i - 1)
                break
        
        return random.choice(card_range)