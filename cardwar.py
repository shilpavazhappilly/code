#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

mycards = [(s,r)for s in SUITE for r in RANKS]

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Creating new ordered Deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]
    def shuffle(self):
        print("shuffling")
        shuffle(self.allcards)
    def spilthalf(self):
        return(self.allcards[:26], self.allcards[26:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards = cards
    def __str__(self):
        return "Containing {} cards".format(len(self.cards))
    def add(self, addedcards):
        self.cards.extend( addedcards)
    def removecard(self):
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name ,hand):
        self.name = name
        self.hand = hand
    def play_card(self):
        drawn_card = self.hand.removecard()
        print(" Player {} has placed {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card
    def remove_war_card(self):
        war_cards = []
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.removecard())

            return war_cards
    def stillhavecard(self):
        return len(self.hand.cards)!=0




######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

new_deck = Deck()                                                               #Creating a new deck
new_deck.shuffle()                                                              #shuffling cards
half1, half2 = new_deck.spilthalf()                                                 # spiliting cards for players
computer = Player("Computer",Hand(half1))                                       # half cards assigned to computer
p_name = input(" What is Your name: ")
player1 = Player(p_name,Hand(half2))                                            # half cards assigned to player

total_round = 0
war_count = 0
# start playing

while player1.stillhavecard() and computer.stillhavecard():                     # check if both player and computer have card in hand
    total_round+=1
    print(" New round starts here")
    print(" The current standings: ")
    print("{} curently have {} ".format(player1.name, len(player1.hand.cards)))
    print("{} curently have {} ".format(computer.name, len(computer.hand.cards)))
    print(" Play a card now \n")


    table_cards = []
    c_cards = computer.play_card()
    p_cards = player1.play_card()
    table_cards.append(c_cards)
    table_cards.append(p_cards)

    if c_cards[1]== p_cards[1]:                                                  #comparing the rankings of cards
        war_count+=1

        print("WAR!!!!!!!!")
        table_cards.extend(player1.remove_war_card())
        table_cards.extend(computer.remove_war_card())

        if RANKS.index(c_cards[1])<RANKS.index(p_cards[1]):
            player1.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)
    else:
        if RANKS.index(c_cards[1])<RANKS.index(p_cards[1]):
            player1.hand.add(table_cards)
        else:
            computer.hand.add(table_cards)

print("GAME OVER!!!!\n")
print("Number rounds played : "+str(total_round))
print("War happened "+str(war_count) )
print(" Does computer have cards?")
print(str(computer.stillhavecard()))
print(" Does Player have cards?")
print(str(player1.stillhavecard()))
