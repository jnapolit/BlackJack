#CREATOR: Jessica Napolitano
#FUNCTION: This class creates a Deck which is just a list of playing cards.
#This class utalizes the PlayingCard class. It includes the methods of: shuffle
#which randomizes all the playing cards in the list, dealCard which pops the first
#card off the deck and returns it, and cardsLeft which returns the number of playing
#cards left in the deck. 

from playingcardsclass import PlayingCard
from random import *


class Deck:

    def __init__(self):

        #for each suit in the list and each rank in the list append the rank and suit combination possibilities
        self.cardList = []
        for s in ['d','c','h','s']:
            for r in range(2,15): # had to be shift by one because our program is adding +1 to each 2-9 card
                self.cardList.append(PlayingCard(r,s))

        
    def shuffled(self):

        #randomization method used to shuffle the cards in the list
        shuffle(self.cardList)

    def dealCard(self):

        #the first card in the list is removed and its value is returned
        popCard = self.cardList.pop(0)
        return popCard 
        
    
    def cardsLeft(self):

        #the length of the list is analyzed and the remaining number of cards is returned
        numCards = len(self.cardList)
        return numCards



def test():

    deck = Deck()
    print(deck)

    #test code that was commented out
    """n=eval(input('number of cards: '))
    for i in range(n):
        x=Deck(cardList).dealCard()
        print (x)"""
    
    deck.shuffled()
    print("____________________________________________")
    deck.dealCard()
    print("___________________________________________")
    deck.cardsLeft()
    

if __name__ == "__main__":
    test()
