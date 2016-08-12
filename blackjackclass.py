#CREATOR: Jessica Napolitano
#FUNCTION: Creates functions to be used in the application such as inital deal which
#initally deals the first two cards to both the computer and player, hit which will
#give another card to the player (note this function is only for the player), and 
#evalute hand which given a hand will determine it's total BJ value (note this function
#takes into account whether an Ace should be counted as a 1 or 11, and DealerPlays
#simulates the moves the computer will do as the dealer, so as long as it is
#under 17, it will continue to hit. 

from graphics import *
from random import *
from playingcardsclass import *
from deckclass import *

class BlackJack:

    #the class constructor uses accepts player and dealer list and sets to empty
    def __init__(self,dHand=[],pHand=[]):

        #playing deck instance variable created and shuffled using deck class method
        self.playingDeck = Deck()
        self.playingDeck.shuffled()

        #instance variable of dealer and player hand created
        self.dHand = dHand
        self.pHand = pHand
                 

    #the initial dealing of cards method is created
    def initDeal(self,gwin,xposD,yposD,xposP,yposP):
        
        #two cards are added to the player hand list
        self.pHand.append(self.playingDeck.dealCard())
        self.pHand.append(self.playingDeck.dealCard())

        #two cards are added to the dealer hand list
        self.dHand.append(self.playingDeck.dealCard())#first of dealer
        self.dHand.append(self.playingDeck.dealCard())#second of dealer

        #Draws the dealers first card face down
        imD1 = Image(Point(xposD, yposD), 'playingcards/b1fv.gif')
        imD1.draw(gwin)

        #draws the dealers second card image face up
        imD2 = Image(Point(xposD + 40, yposD),'playingcards/'+ self.dHand[1].getSuit() + str(self.dHand[1].getRank()) +'.gif')
        imD2.draw(gwin)

        #draws the players first and second card image face up
        imP1 = Image(Point(xposP, yposP),'playingcards/'+ self.pHand[0].getSuit()+ str(self.pHand[0].getRank()) +'.gif')
        imP1.draw(gwin)
        imP2 = Image(Point(xposP + 40, yposP),'playingcards/'+ self.pHand[1].getSuit()+ str(self.pHand[1].getRank()) +'.gif')
        imP2.draw(gwin)

    #creates the hit method
    def hit(self,gwin,xPos,yPos):

        #a card from the deck class is appended to the players hand instance variable
        #and corresponding card image is placed on windpw
        self.pHand.append(self.playingDeck.dealCard())
        imP = Image(Point(xPos,yPos),'playingcards/'+ self.pHand[-1].getSuit() + str(self.pHand[-1].getRank()) + '.gif')
        imP.draw(gwin)
                          

    #evalute hand method is created
    def evaluteHand(self, hand):
        
        total = 0
        #for every card in the hand list
        for cards in hand:

            #if the card is an ace
            if cards.getRank() == 1:

                #the total is increased by 11
                total = total + 11
            else:
                
                #if its not an ace then add their blackjack values to the total
                total = total + cards.BJValue()
                
        #if the total at this point is greater than 21..              
        if total > 21:

            #search through all the cards in the hand...
            for cards in hand:

                #if you find and ace
                if cards.getRank() == 1:
                    
                    #subtract 10 from the total
                    total = total - 10
                    
        #return the total to where its called
        return total

    #dealerplays method is created and take coordinates for card object positions
    def DealerPlays(self, gwin, xPos,yPos):

        #creates the new x position for new card object dealt
        newPosX = xPos
        count = 0
        
        #while the total of the dealers hand is less than 17....
        while self.evaluteHand(self.dHand) < 17:


            #a new playing card is added to the dealer hand and the coresponding image will be shown at a new position
            self.dHand.append(self.playingDeck.dealCard())
            imP = Image(Point(newPosX,yPos),'playingcards/'+ self.dHand[-1].getSuit() + str(self.dHand[-1].getRank()) + '.gif')
            newPosX = newPosX + 75
            imP.draw(gwin)
        
  
def test():

   
    gwin=GraphWin("Black Jack", 600,600)

    pHand=[]
    dHand=[]
    myBlackJack=BlackJack(dHand,pHand)
##    myBlackJack.initDeal(gwin,100,100,100,400)
##    
##    myBlackJack.hit(gwin,220,400)
##    myBlackJack.hit(gwin,260,400)
##
##    pScore = Text(Point(70,500), "Player Score: " )
##    pScore.draw(gwin)
##    #myBlackJack.evaluteHand(pHand)
##    
##    print("________________________________")
##    
##    print('dealer')
##    myBlackJack.evaluteHand(dHand)

    myBlackJack.DealerPlays(gwin,220,100)
    
    
    
    

if __name__ == "__main__":
    test()

