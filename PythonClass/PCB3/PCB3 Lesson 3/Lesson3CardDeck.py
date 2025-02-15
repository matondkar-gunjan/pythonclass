from random import shuffle
class Card:
      def __init__(self, suit, value):
            self.suit = suit
            self.value = value
      def __repr__(self):
            return "{} of {}".format(self.value, self.suit)
class Deck:
      def __init__(self, suits, values, cards):
            self.suits = suits
            self.values = values
            self.cards = cards
      def shuffle(self):
            shuffle(self.cards)
            return self
      def deal(self):
            if len(self.cards) > 1:
                  return self.cards.pop()
      def card_remaining(self):
            print("\nHere are the cards remaining in the deck:")
            for card in self.cards:
                  print(card)
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
cards = [Card(suit, value) for suit in suits for value in values]
deck = Deck(suits, values, cards)
cards_drawn = []

for i in range(13):
      deck.shuffle()
      cards_drawn.append(deck.deal())

print("Cards drawn")
for card in cards_drawn:
      print(card)
deck.card_remaining()
