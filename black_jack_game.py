suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


import random
class Deck:

    def __init__(self):
        self.all_cards=[]


        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)

                self.all_cards.append(created_card)

    def __str__(self):
        deck_comp=''
        for i in self.all_cards:
            deck_comp += '\n'+ i.__str__()
        return deck_comp

    def deal(self):
        return self.all_cards.pop()

    def shuffle(self):
        random.shuffle(self.all_cards)




class Hand:

    def __init__(self):
        self.card=[]
        self.value=0
        self.aces=0

    def add_card(self,new_card):
         self.card.append(new_card)
         self.value=self.value+values[new_card.rank]
         if new_card.rank=="Ace":
             self.aces+=1
         else:
             pass

    def adjust_for_ace(self):
        if self.aces!=0:
            if self.value>21:
                self.value=self.value-10
            else:
                pass
        else:
            pass

class Chips:

    def __init__(self):
        self.total=200
        self.bet=0

    def win_bet(self):
        self.total=self.total+((self.bet)*2)

    def lose_bet(self):
        self.total=self.total - self.bet


def take_bet(chips):
    chips.bet=0
    while True:
        try:
            chips.bet=int(input("place a bet : "))
        except:
            print('you did not enter an integer')
            continue
        else:
            if chips.bet<=chips.total:
                return chips.bet
                print(f'{chips.bet} bet is placed')
                break
            else:
                print('player doesnt have this many chips to bet')
                continue

def hit(deck,hand):

    if hand.value<21:
       hand.add_card(deck.deal())
       hand.adjust_for_ace()


def hit_or_stand(deck,hand):



    while True:
        x=input(' hit or stand? enter h or s: ')

        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            playing = False
        else:
            print('enter h or s')
            continue
        break
    return x

#card
#newdeck=Deck()
#hand=Hand()
#hit_or_stand(newdeck,hand)
#print(hand.card)


def show_some(player,dealer):

    dealer_visible_cards=dealer.card[1]



    print(f'player has :',*player.card ,sep='\n')
    print(f'dealer has {dealer_visible_cards}')


def show_all(player,dealer):

    print('player has: ', *player.card ,sep='\n')
    print(f'value {player.value}')
    print(f'dealer has:', *dealer.card ,sep='\n')
    print(f'value {dealer.value}')


def player_bust(player,chips):

    print('player BUST! \ndealer wins')

    chips.lose_bet()


def player_wins(player,chips):
    print('player wins')
    chips.win_bet()



def dealer_bust(dealer,chips):
    print('dealer BUST! \nplayer wins')
    chips.win_bet()

def dealer_wins(dealer,chips):
    print('dealer wins')
    chips.lose_bet()



def push(palyer,dealer):
    print('player and dealer tie!')


def replay():

    answer=''

    while answer not in ['Y','N']:
        answer=input('Do want to play again?\nY or N: ')

        if answer in ['Y','N']:
            pass
        else:
            print('choose Y or N')
        if answer=='Y':
            playing= True
        elif answer=='N':
            playing=False

    return playing

global playing
while True:


    print('Welcome to Black Jack Game!')
#Creating the deck
    new_deck=Deck()
    new_deck.shuffle()
#setting up the player and dealer
    player1=Hand()
    dealer=Hand()
#dealing card to player
    player1.add_card(new_deck.deal())
    player1.add_card(new_deck.deal())

#dealing cards to dealer
    dealer.add_card(new_deck.deal())
    dealer.add_card(new_deck.deal())
#setting up chips
    chips=Chips()
#taking bet
    take_bet(chips)

    show_some(player1,dealer)
    playing =True



    while playing:
        
        if hit_or_stand(new_deck,player1)=='s':
            playing=False
        else:
            pass

        show_some(player1,dealer)

        if player1.value >21:
            break

    if player1.value < 21:
       while dealer.value<17:
             hit(new_deck,dealer)
       show_all(player1,dealer)

       if dealer.value >21:
            dealer_bust(dealer,chips)

       elif dealer.value > player1.value:
            dealer_wins(dealer,chips)

       elif player1.value> dealer.value:
            player_wins(player,chps)

       else:
            push(player1,dealer)



    print(f'you have a total of {chips.total} chips')

    if not replay():
        break
