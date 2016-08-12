#CREATOR: Jessica Napolitano
#FUNCTION: Creates a playing card which has the accessor
#methods to return the rank, suit, and BlackJack value
#of the specific playing card

from graphics import*
from random import*

class PlayingCard:

    #creates the playing card class with rank and suit parameters
    def __init__(self,rank,suit):

        #the rank and suit instance variables are created
        self.rank = rank - 1
        self.suit = suit

    #get rank method is created
    def getRank(self):
        return self.rank

    #get suit method is created
    def getSuit(self):
        return self.suit

    #this allows us to create the deck of playing cards based on rank list and suit dictionary
    def __str__(self):
        rankList = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        suitList = {'s':'spade','c':'clubs','h':'hearts', 'd':'diamonds'}

        #returs the string message 'rank of suit'
        return rankList[self.getRank()] + ' of ' + suitList[self.getSuit()]

    #assigns each card a blackjack value via method
    def BJValue(self):

        #if rank is 10 or face card its value is 10
        if self.getRank() >= 10:
            self.rank = 10
            
        #else the card uses its normal face value
        else:
            self.rank = self.rank 

        #and at the end we return the rank    
        return self.rank

def test():
    c= PlayingCard(12,'d')
    print(c)
    value=PlayingCard(3,'d').BJValue()
    print(value)
    
if __name__=="__main__":
    test()
    
    
