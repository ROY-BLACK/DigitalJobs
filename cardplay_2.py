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
    ACE = 14

class HandRank(Enum):
    """enumeration of the types of possible poker hands"""
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9

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

    def __eq__(self, other):
        #return self.rank == other.rank and self.suit == other.suit
        return self.rank == other.rank

    def __lt__(self, other):
        if self.rank.value < other.rank.value:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.rank.value > other.rank.value:
            return True
        else:
            return False

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
    def __init__(self, deck, hand_size=5):
        self.cards = deck.drawX(hand_size)
        if self.cards == None:
            print('Unable to draw {} cards from {}'.format(hand_size, deck))

    def __str__(self):
        temp = ''
        for card in self.cards:
            temp += '  {}'.format(card)
        return temp

    def sort(self):
        self.cards.sort()

    def score_hand(self):
        temp_hand = self
        temp_hand.sort()

        #high_card = temp_hand.cards[-1].rank.value
        high_card = max(temp_hand.cards)
        print('High card? ', high_card.rank.name.capitalize())

        flush = True
        temp_suit = None
        for card in temp_hand.cards:
            if temp_suit == None:
                temp_suit = card.suit
            else:
                if temp_suit == card.suit:
                    continue
                else:
                    flush = False
                    break
        print('Flush? ', flush)

        straight = True
        curr_rank = 0
        for card in temp_hand.cards:
            if curr_rank == 0:
                curr_rank = card.rank.value
            else:
                if (curr_rank + 1) == card.rank.value:
                    curr_rank += 1
                    continue
                else:
                    straight = False
                    break
        print('Straight? ', straight)

        straight_flush = straight and flush
        royal_flush = straight_flush and high_card.rank.value == 14

        print('Straight flush? ', straight_flush)
        print('Royal flush? ', royal_flush)

        first_four = temp_hand.cards[0].rank.value == temp_hand.cards[-2].rank.value
        last_four = temp_hand.cards[1].rank.value == temp_hand.cards[-1].rank.value
        four_of_a_kind = first_four or last_four
        #temp_card = None
        #for card in temp_hand.cards[:4]:
        #    if temp_card == None:
        #        temp_card = card
        #    else:
        #        if card.rank.value == temp_card.rank.value:
        #            continue
        #        else:
        #            first_four = False
        #            break
        first_three = temp_hand.cards[0].rank.value == temp_hand.cards[2].rank.value
        middle_three = temp_hand.cards[1].rank.value == temp_hand.cards[3].rank.value
        last_three = temp_hand.cards[2].rank.value == temp_hand.cards[4].rank.value
        three_of_a_kind = first_three or middle_three or last_three

        first_two = temp_hand.cards[0].rank.value == temp_hand.cards[1].rank.value
        second_two = temp_hand.cards[1].rank.value == temp_hand.cards[2].rank.value
        third_two = temp_hand.cards[2].rank.value == temp_hand.cards[3].rank.value
        fourth_two = temp_hand.cards[3].rank.value == temp_hand.cards[4].rank.value
        pair = first_two or second_two or third_two or fourth_two

        full_house = False
        if first_three and fourth_two or last_three and first_two:
            full_house = True

        two_pair = False
        if not four_of_a_kind and not three_of_a_kind:
            two_pair = (first_two and (third_two or fourth_two)) or (second_two and (fourth_two))

        if straight_flush:
            return HandRank(9)
        if four_of_a_kind:
            return HandRank(8)
        elif full_house:
            return HandRank(7)
        elif flush:
            return HandRank(6)
        elif straight:
            return HandRank(5)
        elif three_of_a_kind:
            return HandRank(4)
        elif two_pair:
            return HandRank(3)
        elif pair:
            return HandRank(2)
        else:
            return HandRank(1)


    #"""enumeration of the types of possible poker hands"""
    #HIGH_CARD = 1
    #PAIR = 2
    #TWO_PAIR = 3
    #THREE_OF_A_KIND = 4
    #STRAIGHT = 5
    #FLUSH = 6
    #FULL_HOUSE = 7
    #FOUR_OF_A_KIND = 8

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

if __name__ == '__main__':
    deck = Deck(Standard_52_Card_Deck)
    deck.shuffle()
    hand = Hand(deck)
    hand.sort()
    print(hand)
    print(hand.score_hand().name)
