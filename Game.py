from Deck import Deck
from Card import Card
import time

# TODO: 
# 1. Finish Game
# 2. Add Double Down and Split Hands
# 3. Add Insurance


MIN_BET = 25
STARTING_MONEY = 200

class Game:
    def __init__(self):
        self.money = STARTING_MONEY
        self.deck = Deck()
        self.dealer_hand = []
        self.player_hand = []
        
    def __restart_game(self):
        time.sleep(1)
        print("Restarting game now")
        self.deck = Deck()
        self.dealer_hand = []
        self.player_hand = []
        print()
        time.sleep(2)
    
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
    
    def __print_hand(self, hand, player):
        string = str(hand[0])
        for i in range(1, len(hand)):
            card = hand[i]
            string = string + ", " + str(card)
        if player:
            print(f"Your hand is: {string}")
        else:
            print(f"Dealer's hand is: {string}")
        
    def __sum_hand(self, hand):
        sum = 0
        aces = 0
        for card in hand:
            sum = sum + card.get_value()
            if card.get_symbol() == "A":
                aces = aces + 1
        for i in range(aces):
            if ((sum - 10) <= 21) and (sum > 21):
                sum = sum - 10
        print("sum = ", sum)
        return sum
    
    def run_game(self, bet):
        print()
        self.deck.shuffle()
        self.__create_hands()
        
        print(f"Dealer is showing: {self.dealer_hand[0]}")
        self.__print_hand(self.player_hand, True)
        
        # these check if the starting hands have blackjack, and end the game if they do
        BJ = self.__check_BJ()
        if BJ == "Player":
            print("Congratulations, you have BlackJack!!!")
            self.money = self.money + (bet * 1.5)
            self.__print_money()
            self.__restart_game()
            return
        elif BJ == "Dealer":
            print("Dealer got BlackJack. Better luck next time!")
            self.money = self.money - bet
            self.__print_money()
            self.__restart_game()
            return
        elif BJ == "Draw":
            print("Looks like it's a draw with BlackJacks")
            self.__print_money
            self.__restart_game()
            return
        
        hit = True
        while hit:
            print()
            hit = None
            while hit == None:
                hit = input("Would you like to hit? (Y/N): ")
                if (hit == "Y" or hit == "y"):
                    hit = True
                elif(hit == "N" or hit == "n"):
                    hit = False
                else:
                    print("Please input either Y or N")
                    hit = None
                time.sleep(1)
                    
            if hit:
                self.player_hand.append(self.deck.pop())
                self.__print_hand(self.player_hand, True)
                if self.__sum_hand(self.player_hand) > 21:
                    print("You bust!")
                    self.money = self.money - bet
                    self.__print_money()
                    self.__restart_game()
                    return
            time.sleep(2)

        self.__print_hand(self.dealer_hand, False)
        time.sleep(1)
        
        while self.__sum_hand(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())
            print("Dealer hits and his new hand is:")
            time.sleep(1)
            self.__print_hand(self.dealer_hand, False)
            print()
            time.sleep(5)
            
        dealer_sum = self.__sum_hand(self.dealer_hand)
        player_sum = self.__sum_hand(self.player_hand)
        
        if (dealer_sum < player_sum) or dealer_sum > 21:
            print("Congratulations, you win!")
            self.money = self.money + bet
            self.__print_money()
        elif dealer_sum > player_sum:
            print("You lose!")
            self.money = self.money - bet
            self.__print_money()
        else:
            print("You draw!")
            self.__print_money()
        
        self.__restart_game()
        
        
            
        
        

        
def main():
    game = Game()
    print(f"You get ${STARTING_MONEY} to start with. Have fun!")
    print()
    play = True
    count = 0
    while(play != None):
            play = input("Would you like to play a game of Blackjack? (Y/N): ")
            if (play == "Y" or play == "y"):
                play = None
            elif(play == "N" or play == "n"):
                print("Have a good day!")
                playe = False
                break
            else:
                print("Please input either Y or N")
                play = True
    while(play == None):
        if count == 0:
            play = True
        count = count + 1
        # asks player if they wanna play blackjack. they have to input either Y, y, N, or n
        while(play == None and count > 1):
            play = input("Would you like to play another round? (Y/N): ")
            if (play == "Y" or play == "y"):
                play = True
            elif(play == "N" or play == "n"):
                play = False
            else:
                print("Please input either Y or N")
                play = None
        if not play and count > 1:
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
            elif bet > game.money:
                print(f"Please input a bet that is less than or equal to ${game.money}")
                bet = None
        if(play):
            game.run_game(bet)
            play = None
    
    
    
if __name__ == "__main__":
    main()