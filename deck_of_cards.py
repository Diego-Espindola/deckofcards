# This is a sample Python script about OOP.

class Card(object):
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        pass


class Player(object):
    def __init__(self):
        pass



car = Card("Clubs", 6)
car.show()