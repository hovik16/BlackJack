from Card import Card
import random

class Deck:
    def __init__(self):
        self.deck = []
        symbols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        suits = ["Heart", "Spade", "Club", "Diamond"]
        for suit in suits:
            for sym in symbols:
                self.deck.append(Card(sym, suit))
                
    def print(self):
        for card in self.deck:
            print(card)
    
    def pop(self):
        return self.deck.pop()
    
    def shuffle(self):
        random.shuffle(self.deck)