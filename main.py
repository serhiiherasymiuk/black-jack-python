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


def play_blackjack():
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    # Initial deal
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    # Show hands
    print("Dealer's Hand:")
    print(dealer_hand.cards[0])  # Show only one of the dealer's cards
    print("\nPlayer's Hand:")
    print(player_hand)
    player_hand.calculate_value()

    # Player's turn
    while player_hand.value < 21:
        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.add_card(deck.deal_card())
            print("\nPlayer's Hand:")
            print(player_hand)
            player_hand.calculate_value()
        elif choice == 's':
            break
        else:
            print("Invalid choice!")

    # Check if player busted
    if player_hand.value > 21:
        print("You busted! Dealer wins.")
        return

    # Dealer's turn
    print("\nDealer's Turn:")
    print("Dealer's Hand:")
    print(dealer_hand)
    dealer_hand.calculate_value()
    while dealer_hand.value < 17:
        dealer_hand.add_card(deck.deal_card())
        print("\nDealer hits:")
        print("Dealer's Hand:")
        print(dealer_hand)
        dealer_hand.calculate_value()

    # Determine the winner
    if dealer_hand.value > 21 or player_hand.value > dealer_hand.value:
        print("Player wins!")
    elif player_hand.value < dealer_hand.value:
        print("Dealer wins!")
    else:
        print("It's a tie!")



if __name__ == "__main__":
    play_blackjack()
