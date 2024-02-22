import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        ace_count = 0
        for card in self.cards:
            if card.rank.isdigit():
                self.value += int(card.rank)
            elif card.rank in ['Jack', 'Queen', 'King']:
                self.value += 10
            else:  # Ace
                ace_count += 1
                self.value += 11

        # Adjust for aces
        while self.value > 21 and ace_count > 0:
            self.value -= 10
            ace_count -= 1

    def __str__(self):
        hand_str = ""
        for card in self.cards:
            hand_str += str(card) + "\n"
        return hand_str


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    player_hand.calculate_value()

    print("Player's Hand:")
    print(player_hand)
    print("Total Value:", player_hand.value)
