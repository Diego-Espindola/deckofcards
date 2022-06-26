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

    def draw(self):
        return self.cards.pop()


class Player(object):
    def __init__(self):
        pass


# card = Card("Clubs", 6)
# card.show()

deck = Deck()
deck.shuffle()
deck.show()

card = deck.draw()
card.show()
