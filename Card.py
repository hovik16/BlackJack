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
    
    def get_symbol(self):
        return self.symbol
    def get_suit(self):
        return self.suit
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