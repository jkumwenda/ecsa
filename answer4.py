class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Deck:
    def __init__(self):
        self.cards = []

    def shuffle(self):
        # Shuffle the deck code here
        pass

    def draw_card(self):
        # Draw a card from the deck code here
        pass

    def cards_left(self):
        # Return the number of cards left in the deck code here
        pass


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        # Add a card to the hand code here
        pass

    def calculate_score(self):
        # Calculate the score of the hand code here
        pass
