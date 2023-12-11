from Deck import Deck
from Card import Card

# TODO: 
# 1. Add Double Down and Split Hands
# 2. Finish Game


MIN_BET = 25

class Game:
    def __init__(self):
        self.money = None
        while(self.money == None):
            self.money = input("How much money are you starting with? ")
            self.money = int(self.money)
            if(not isinstance(self.money, int)):
                print("Please input a valid value")
                self.money = None 
        self.deck = Deck()
        self.dealer_hand = []
        self.player_hand = []
        
    def __restart_game(self):
        self.deck = Deck()
        self.dealer_hand = []
        self.player_hand = []
        print()
    
    def __create_hands(self):
        # creates dealer's hand
        self.dealer_hand.append(self.deck.pop())
        self.dealer_hand.append(self.deck.pop())
        
        # creates player's hand
        self.player_hand.append(self.deck.pop())
        self.player_hand.append(self.deck.pop())
        
    def __check_BJ(self):
        dealer_sum = 0 
        player_sum = 0
        for card in self.dealer_hand:
            dealer_sum = dealer_sum + card.get_value()
        for card in self.player_hand:
            player_sum = player_sum + card.get_value()
            
        
        BJ = (dealer_sum == 21) and (len(self.dealer_hand) == 2)
        if((player_sum == 21) and (len(self.player_hand) == 2) and BJ):
            return "Draw"
        elif((player_sum == 21) and (len(self.player_hand) == 2)):
            return "Player"
        elif(BJ):
            return "Dealer"
        else:
            return None
    
    def __print_money(self):
        print(f"You now have ${self.money}")
    
    def __print_player_hand(self):
        string = str(self.player_hand[0])
        for i in range(1, len(self.player_hand)):
            card = self.player_hand[i]
            string = string + ", " + str(card)
        print(f"Your hand is: {string}")
    
    def __print_dealer_hand(self):
        string = str(self.dealer_hand[1])
        for i in range(2, len(self.player_hand)):
            card = self.player_hand[i]
            string = string + ", " + str(card)
        print(f"Dealer is showing: {string}")
    
    def run_game(self, bet):
        print()
        self.deck.shuffle()
        self.__create_hands()
        
        self.__print_dealer_hand()
        self.__print_player_hand()
        
        # these check if the starting hands have blackjack, and end the game if they do
        BJ = self.__check_BJ()
        if BJ == "Player":
            print("Congratulations, you have BlackJack!!!")
            self.money = self.money + (bet * 1.5)
            self.__print_money()
            return
        elif BJ == "Dealer":
            print("Dealer got BlackJack. Better luck next time!")
            self.money = self.money - bet
            self.__print_money()
            return
        elif BJ == "Draw":
            print("Looks like it's a draw with BlackJacks")
            self.__print_money
            return
        
        # ADD DOUBLE DOWN AND SPLIT HANDS HERE
        
        self.__restart_game()
        
        
            
        
        

        
def main():
    game = Game()
    while(True):
        # asks player if they wanna play blackjack. they have to input either Y, y, N, or n
        play = None
        while(play == None):
            play = input("Would you like to play Blackjack? Y/N ")
            if (play == "Y" or play == "y"):
                play = True
            elif(play == "N" or play == "n"):
                play = False
            else:
                print("Please input either Y or N")
                play = None
        if not play:
            print("Have a good day!")
            break 
        
        bet = None
        while(bet == None):
            bet = input(f"Minimum Bet is ${MIN_BET}. How much money are you betting? ")
            bet = int(bet)
            if(not isinstance(bet, int)):
                print("Please input a valid value")
                bet = None
            elif bet < MIN_BET:
                print(f"Please input a bet that is at least ${MIN_BET}")
                bet = None
        if(play):
            game.run_game(bet)
    
    
    
if __name__ == "__main__":
    main()