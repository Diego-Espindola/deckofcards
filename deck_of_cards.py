# This is a sample Python script about OOP.
import random


class Card(object):
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw_card(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, d):
        self.hand.append(d.draw_card())
        return self.hand

    def show_hand(self):
        for c in self.hand:
            c.show()

    def discard(self, suit, value):
        # TODO maybe try to search a card in the deck by suit and value previously informed
        for c in self.hand:
            pass

    def deal_cards(self, d, total):
        for x in range(0, total):
            self.draw(d)
        for card in self.hand:
            print("{} of {}".format(card.value, card.suit))


deck = Deck()
deck.shuffle()

diego = Player("Diego")

diego.deal_cards(deck, 11)



