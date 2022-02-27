#THE DICTIONARY OF CORRESPONDING RANK VALUES
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}
#THE LIST OF SUITS
suits = ['Hearts',"Diamonds","Spades","Clubs"]
#THE LIST OF RANKS
ranks = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
import random
import sys #imported libraries
class Deck(): #class to operate the Deck
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                    #Create the card object
                createdcard = Card(suit,rank)
                self.allcards.append(createdcard)
    def shufflecards(self):
        random.shuffle(self.allcards)
        return self.allcards
    def dealone(self):
        return self.allcards.pop()
class Card(): #class to operate the cards
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
class Player(): #class to manipulate player
    def __init__(self,name):
        self.name = name
        self.allcards = []
    def removeone(self):
        try:
            return self.allcards.pop()
        except Exception:
            print("This is an empty list!")
            sys.exit()
    def addcards(self,newdeck):
        if(type(newdeck)==type([])):
            self.allcards.extend(newdeck)
        else:
            self.allcards.append(newdeck)
    def __str__(self):
        return f"{self.name} has {len(self.allcards)} cards"
playerone = Player("One")
playertwo = Player("Two")

new_deck = Deck()
new_deck.shufflecards()

for x in range(26):
    playerone.addcards(new_deck.dealone())
    playertwo.addcards(new_deck.dealone())

game_on = True

round_num = 0
while game_on:
    round_num+=1
    print(f"Round {round_num} has started!")
    if(len(playerone.allcards)==0):
        print("Player one out of cards! Player Two wins!")
        game_on = False
        break
    elif(len(playertwo.allcards) == 0):
        print("Player two out of cards! Player one wins!")
        game_on = False
        break


    playeronecards = []
    playeronecards.append(playerone.removeone())
    playertwocards = []
    playertwocards.append(playertwo.removeone())

    at_war = True
    while at_war:
        if playeronecards[-1].values>playertwocards[-1].values:
            playerone.addcards(playeronecards)
            playerone.addcards(playertwocards)
            at_war = False
        elif playertwocards[-1].values<playeronecards[-1].values:
            playertwo.addcards(playertwocards)
            playertwo.addcards(playeronecards)
            at_war = False
        else:
            print("WAR!")
            if len(playerone.allcards)<5:
                print('Player one is unable to play a war!')
                print('Player two wins!')
                game_on = False
                break
            elif len(playertwo.allcards)<5:
                print('Player two is unable to play a war!')
                print('Player one wins!')
                game_on = False
                break
            else:
                for num in range(3):
                    playeronecards.append(playertwo.removeone())
                    playertwocards.append(playertwo.removeone())
