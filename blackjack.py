import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.deck.append(card)
    
    def __str__(self):
        cards = '' 
        for card in self.deck:
             cards += '\n '+card.__str__()
        return cards

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value = self.value + values[card.rank]
        if card.rank == 'Ace':
            self.aces = self.aces + 1
    
    def adjust_for_ace(self):
        while self.aces > 0 and self.value> 21:
            self.value = self.value - 10
            self.aces = self.aces - 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        
    def __str__(self):
        return '\nYou have {} Chips.'.format(self.total)

def take_bet(chips):
    
    takebet = True
    while takebet:
        try:
            chips.bet = int(input('Please enter a bet (digit): '))
            if chips.bet <= chips.total:
                takebet = False
        except:
            print('Must be an integer.')
        else:
            if chips.bet > chips.total:
                print('Chips cannot exceed',chips.total)
    return chips.bet

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        
        decision = input('Hit or Stand? H/S: ').upper()
        
        if decision == 'H':
            print('Hit!')
            hit(deck,hand)
            show_some(player,dealer)
            #show_all(player,dealer)
        elif decision == 'S':
            print('\nPlayer stands. Dealer is playing.')
            playing = False
        else:
            print('Please type H or S')
            continue
        break

def show_some(player,dealer):
    
    print("\nDealer's Hand: <card hidden>, {}".format(dealer.cards[1]))
    print("Player's Hand: ",*player.cards, sep=', ')
    print("Player's value", player.value,'\n')
    
def show_all(player,dealer):
    
    print("Player's Hand: ",*player.cards, sep=', ')
    print("Player's value", player.value,'\n')
    print("Dealer's Hand: ",*dealer.cards, sep=', ')
    print("Dealer's value", dealer.value)

def player_busts(player,dealer,chips):
    print('Player bust.\n')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player wins.\n')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Dealer busts.\n')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('Dealer wins.\n')
    chips.lose_bet()
    
def push(player,dealer,chips):
    print('Dealer and Player ties.')

gameon = True
playerchips = Chips()

while gameon:
    # Print an opening statement
    print('\nWelcome to blackjack!')

    # Create & shuffle the deck, deal two cards to each player
    newdeck = Deck()
    newdeck.shuffle()
    
    dealer = Hand()
    player = Hand()
    
    for i in range(2):
        dealer.add_card(newdeck.deal())
        player.add_card(newdeck.deal())
    
        
    # Set up the Player's chips
    print('You start with {} Chips!'.format(playerchips.total))
    
    
    # Prompt the Player for their bet 
    betvalue = take_bet(playerchips)
    playerchips.bet = betvalue

    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    #show_all(player,dealer)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(newdeck,player)
        
        # Show cards (but keep one dealer card hidden)
        #show_some(player,dealer)
 
        # If player's hand exceeds 21, run player_busts() and break out of loop       
        if player.value > 21:
            player_busts(player,dealer,playerchips)
            
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

    if player.value < 22:
        while dealer.value <17:
            hit(newdeck,dealer)

        # Show all cards
        show_all(player,dealer)

        # Run different winning scenarios

        if dealer.value > 21:
            dealer_busts(player,dealer,playerchips)

        elif player.value > dealer.value:
            player_wins(player,dealer,playerchips)

        elif dealer.value > player.value:
            dealer_wins(player,dealer,playerchips)
        
        else:
            push(player,dealer,playerchips)
    
    # Inform Player of their chips total 
    show_all(player,dealer)
    print(playerchips)
    
    # Ask to play again
    again = input('Would you like to play again? (Y/N)').upper()
    
    if again == 'Y':
        playing = True
        continue
    else:
        gameon = False
        #break
