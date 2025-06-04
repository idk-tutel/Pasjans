class Card:
    def __init__(self, colour, symbol):
        self.colour = colour
        self.symbol = symbol
        self.inv = False
        self.selected = False
        self.coldict = {
            "pik":"♠",
            "trefl":"♣",
            "karo":"♦",
            "kier":"♥"
        }
        if self.colour == "karo" or self.colour == "kier":
            self.red = True
        else: self.red = False
    def printcard(self):
        return self.symbol + self.coldict[self.colour]



