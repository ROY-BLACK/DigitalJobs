from enum import Enum
from enum import auto

class Suit(Enum):
    """enumeration of the suits in a standard 52-card deck"""
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()

class Rank(Enum):
    """enumeration of the ranks in a standard 52-card deck"""
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class TypeOfDeck():
    """Defines the type of deck used in a card game"""
    def __init__(self, name, suit_enum, rank_enum):
        self.name = name
        self.suits = suit_enum
        self.ranks = rank_enum

    def __str__(self):
        return self.name

Standard_52_Card_Deck = TypeOfDeck('Standard 52-card', Suit, Rank)

class Card():
    """Represents a member of a Deck.
       Each Card has a suit and a value.
       Each Card is unique within a Deck."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(self.rank.name.capitalize(), self.suit.name.capitalize())

class Deck():
    """Contains a list of unique Card objects, cards"""
    def __init__(self, deck_type):
        self.deck_type = deck_type
        self.cards = [Card(suit, rank) for suit in deck_type.suits for rank in deck_type.ranks]

    def __str__(self):
        return '{} cards from a {} deck'.format(len(self.cards), self.deck_type.name)

    def shuffle(self):
        """randomize the order of cards"""
        import random
        random.shuffle(self.cards)

    def draw(self):
        try:
            return self.cards.pop(0)
        except IndexError:
            print('draw called on an empty deck')
            return None

    def drawX(self, cards_to_draw):
        """Draws cards_to_draw cards from self.cards
           PRECONDITIONS:
           - cards_to_draw is an integer
           - 0 <= cards_to_draw <= len(self.cards)"""
        try:
            x = int(cards_to_draw)
        except ValueError:
            print("cards_to_draw must be an integer: {} provided".format(cards_to_draw))
            return None

        if x < 0 or x > len(self.cards):
            print("attempted to draw too many cards: {} requested, {} available".format(cards_to_draw, len(self.cards)))
            return None

        temp = []
        i = 0
        while i < cards_to_draw:
            temp.append(self.draw())
            i += 1
        return temp

class CardGame():
    """The Players, Dealers, Decks of Cards, and general rules associated with a card game"""
    def __init__(self, name, player_count=2, uses_dealer=False, deck_type=Standard_52_Card_Deck):
        self.name = name
        self.player_count = player_count
        self.uses_dealer = uses_dealer
        self.deck_type = deck_type

    def __str__(self):
        return '{}-player game of {}'.format(self.player_count, self.name)

class Hand():
    """An individual player's hand of Cards"""
    def __init__(self, hand_size, deck):
        self.cards = deck.drawX(hand_size)
        if self.cards == None:
            print('Unable to draw {} of cards from {}'.format(hand_size, deck))

    def __str__(self):
        temp = ''
        for card in self.cards:
            temp += '  {}'.format(card)
        return temp

    def sort(self):
        pass

class Rules():
    pass

class Player():
    pass

class Dealer():
    pass

class DrawPile():
    pass

class DiscardPile():
    pass

class CardDisplay():
    pass

