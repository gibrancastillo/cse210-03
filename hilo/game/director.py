from game.deck import Deck


class Director:
    """
    A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        score (int): The score for one round of play.
        is_playing (boolean): Whether or not the game is being played.
        deck (Deck): An instance of Deck.
    """

    def __init__(self):
        """
        Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        # The player starts the game with 300 points.
        self.score = 300
        self.is_playing = True
        self.deck = Deck()


    def start_game(self):
        """
        Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # Enhanced game play and game over messages.
        print("\n ------- Have fun playing the 'Hilo Game' -------\n")
        print("++++++++++++++++++++++++++++++++++++")

        #This while loop will control the game.
        while self.is_playing:
            self.guess_hi_or_lo()
            self.do_outputs()
            self.will_you_keep_playing()
        
        print("++++++++++++++++++++++++++++++++++++")
        print("\n ------- Good game. Thanks for playing! -------\n")


    def guess_hi_or_lo(self):
        """
        Ask the player to guess if the next card drawn by the dealer will be higher or lower than 
        the previous one. Points are won or lost based on whether or not the player guessed correctly.

        Args:
            self (Director): An instance of Director.
        """
        the_card_value = self.deck.card_a
        next_card_value = self.deck.card_b

        print(f"The card is: {the_card_value}")

        # The player is asked, "Higher or lower?" at the beginning of each turn. Plus enhanced input validation.
        # The player guesses if the next one will be higher or lower.
        guess_option = input("Higher or lower? [h/l] ").lower()

        #This while loop will make sure that the user enters the right letter either h or l.
        while(guess_option not in("h", "l")):
            guess_option = input("Higher or lower? You must enter 'h' or 'l' ").lower()
        
        # The the next card is displayed.
        print(f"Next card was: {next_card_value}")

        # The player earns 100 points if they guessed correctly.
        # The player loses 75 points if they guessed incorrectly.
        if(guess_option == "l"):
            if(next_card_value < the_card_value):
                self.score += 100
            else:
                self.score -= 75
        elif(guess_option == "h"):
            if(next_card_value > the_card_value):
                self.score += 100
            else:
                self.score -= 75
        
        # move card value B to card value A
        self.deck.card_a = self.deck.card_b

        # picks a new random number for value B and ensures that it isn't the same number as A
        self.deck.card_b = self.deck.draw(self.deck.card_a)


    def do_outputs(self):
        """
        Displays the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your roll score is: {self.score}")
    

    def will_you_keep_playing(self):
        """
        If a player reaches 0 points end the game; otherwise, 
        ask the user if they want to keep playing the Hilo game.

        Args:
            self (Director): An instance of Director.
        """
        self.is_playing = (self.score > 0)

        if not self.is_playing:
            return

        # The player is asked, "Play again?" at the end of each turn. Plus enhanced input validation.
        # If a player has more than 0 points they decide if they want to keep playing.
        play_again = input("Play again? [y/n] ").lower()
        
        #This while loop will make sure that the user enters the right letter either y or n.
        while(play_again not in("y", "n")):
            play_again = input("Play again? You must enter 'y' or 'n' ").lower()
        
        # If the player answers "n" or no, the game is over.
        # If a player decides not to play again the game is over.
        self.is_playing = (play_again == "y")

        if not self.is_playing:
            return
        
        print()
    