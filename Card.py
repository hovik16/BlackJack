class Card:
    def __init__(self, symbol, suit):
        self.symbol = symbol
        self.suit = suit
        self.value = symbol
        if isinstance(symbol, str):
            self.value = 10
        if symbol == "A":
            self.value = 11
            
    def __str__(self):
        return str(self.symbol) + " of " + self.suit
    
    def __repr__(self):
        return str(self.symbol) + " of " + self.suit
    
    # possibles symbols are [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A] and all of them are strings
    def get_symbol(self):
        return self.symbol
    # possibles suits are [Hearts, Diamonds, Spades, Clubs] and all of them are strings
    def get_suit(self):
        return self.suit
    # values go from 1-11, Aces = 11. the sum function in the game file handles the variability of aces
    def get_value(self):
        return self.value
    
    def set_suit(self, suit):
        self.suit = suit
    def set_symbol(self, symbol):
        self.symbol = symbol
        self.value = symbol
        if isinstance(symbol, str):
            self.value = 10
        if symbol == "A":
            self.value = 11