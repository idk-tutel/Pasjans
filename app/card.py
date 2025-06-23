class Card:
    def __init__(self, colour="Lancer", symbol="Lancer"):
        self.colour = colour
        self.symbol = symbol
        self.inv = False
        self.selected = False
        self.coldict = {
            "pik":"♠",
            "trefl":"♣",
            "karo":"♦",
            "kier":"♥",
            "Lancer":"L"
        }
        self.lol = ['A ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', 'J ', 'Q ', "K ", "Lancer"]

        if self.colour == "karo" or self.colour == "kier":
            self.red = True
        else: self.red = False
    def cangoon(self, card) -> bool:
        #return True
        debug1 =self.symbol
        debug2 =card.symbol
        if ((self.red and card.red != True) or (card.red and self.red != True) or card.colour == "Lancer") and self.lol.index(self.symbol)+1 == card.lol.index(card.symbol):
            return True
        else:
            return False
    def printcard(self):
        return self.symbol + self.coldict[self.colour]
    def savecard(self):
        if self.inv:savedcard = "T/"
        else:savedcard = "F/"
        savedcard += str(self.lol.index(self.symbol)+1)
        savedcard += "/"
        savedcard += self.colour
        return savedcard
    def loadcard(self, save):
        save = save.split("/")
        if save[0] == "T":
            self.inv = True
        else:
            self.inv = False
        self.symbol = self.lol[int(save[1])-1]
        self.colour = save[2]
        if self.colour == "karo" or self.colour == "kier":
            self.red = True
        else: self.red = False

