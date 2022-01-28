import random


class Deck:
    """
    A Deck that allows the director to draw a card with a different or random number from 1 to 13.

    The responsibility of a Deck is to draw a ranmdom card number from 1 to 13.
   
    Attributes:
        card_a (int): The first or previous card number of the card drawn.
        card_b (int): The second or current card number of the card drawn.
    """

    def __init__(self):
        """
        Constructs a new instance of Deck with a different or random number from 1 to 13.

        Args:
            self (Deck): An instance of Deck.
        """
        self.card_a = self.draw(0)
        self.card_b = self.draw(self.card_a)

    
    def draw(self, card_a):
        """
        Generates a new random value and takes in the previous card 
        value and generates a new one without considering the previous
        
        Args:
            self for instantiation
            card_a (int): The previously card number picked to be excluded from the deck
        """
        card_range = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        
        if card_a > 0:
            for i in card_range:
                if i == card_a:
                    card_range.pop(i - 1)
                    break
        
        return random.choice(card_range)