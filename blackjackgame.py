from graphics import *
from random import *
from playingcardsclass import *
from deckclass import *
from blackjackclass import *
from buttonclass import *

#Steven Natera(snatera@conncoll.edu) and Jessica Napolitano
#The purpose of this program is play a game of black jack!

#This function will setup a game of blackjack by drawing all the cards, creating the blackjack instance, and doing the inital deal

def BlackJackSetup(gwin):
    #create background
    background = Image(Point(300,300),'background.gif')    
    background.draw(gwin)
    
    #creates the stand button in the activated mode   
    standButton = Button(gwin,Point(250,225),75,50,'Stand')
    standButton.setFill('red')
    standButton.activate()

    #creates the hit button in the activated mode
    hitButton = Button(gwin,Point(350,225),75,50,'Hit')
    hitButton.setFill('red')
    hitButton.activate()

    #creates the exit button in the deactivated mode
    exitButton = Button(gwin,Point(250,550),75,50,'Exit')
    exitButton.setFill('red')
    exitButton.activate()
    
    #creates new game button in the activated mode
    newgameButton = Button(gwin,Point(350,550),75,50,'New Game')
    newgameButton.setFill('red')
    newgameButton.activate()


    #create the player and dealer hand, both have zero cards
    pHand=[]
    dHand=[]

    #begins the blackjack game and creates the game in a graphics window
    myBlackJack = BlackJack(dHand,pHand)
    myBlackJack.initDeal(gwin,100,100,100,400)

    #creates a text for players score
    pScore = Text(Point(120,470), "Player Score: ")
    pScore.setFill("white")
    pScore.setStyle('bold')
    pScore.draw(gwin)
    pScore2 = Text(Point(120,500), "0")
    pScore2.setFill("white")
    pScore2.setStyle('bold')


    #creates a text for dealers score
    dScore = Text(Point(120,167), "Dealer Score: ")
    dScore.setFill("white")
    dScore.setStyle('bold')
    dScore.draw(gwin)
    dScore2 = Text(Point(120,190), " ")
    dScore2.setFill("white")
    dScore2.setStyle("bold")

    #shows the initial hand value of the player
    pScore2.setText(myBlackJack.evaluteHand(pHand))
    pScore2.draw(gwin)

    #determines the black jack value of the second card in the dealers hand
    visibleCard = dHand[1].BJValue()
    dScore2.setText(visibleCard)
    dScore2.draw(gwin)

 

    #starting position for the next set of cards
    xPosP = 220

    return dScore2,pScore2,xPosP,pHand,dHand,newgameButton,hitButton,standButton, exitButton, myBlackJack

def BlackJackGame(gwin):

    #call an instance of BlackJackSetup to set up the game
    dScore2,pScore2,xPosP,pHand,dHand,newgameButton,hitButton,standButton,exitButton, myBlackJack = BlackJackSetup(gwin)

    #get a mouse click on the screen
    pt = gwin.getMouse()

    #while the exit button is not clicked run the following commands
    while exitButton.clicked(pt) == False:


        #if stand button is clicked.....
        if standButton.clicked(pt) == True:

            #stand is deactivated, hit is deactivated
            standButton.deactivate()
            hitButton.deactivate()

            #draws the first card face down and then redraws it face up 
            turnPic = Image(Point(100,100), 'playingcards/' + dHand[0].getSuit() + str(dHand[0].getRank()) + '.gif')
            turnPic.draw(gwin)
            reDrawCard2 = Image(Point(140,100), 'playingcards/'  +dHand[1].getSuit() + str(dHand[1].getRank()) + '.gif')
            reDrawCard2.draw(gwin)

            #updates the hand value of the dealer
            myBlackJack.DealerPlays(gwin,220,100) 
            dScore2.setText(myBlackJack.evaluteHand(dHand))

            
            #determines who wins and prints winnder message
            if myBlackJack.evaluteHand(pHand) > myBlackJack.evaluteHand(dHand) and myBlackJack.evaluteHand(pHand)<=21:
                winnerMSG = Text(Point(300,300),'YOU WIN')
                winnerMSG.setFill('blue')
                winnerMSG.setSize(27)
                winnerMSG.draw(gwin)
                
            elif myBlackJack.evaluteHand(dHand) > myBlackJack.evaluteHand(pHand) and myBlackJack.evaluteHand(dHand)<=21:
                loserMSG = Text(Point(300,300),'SORRY YOU LOSE')
                loserMSG.setFill('red')
                loserMSG.setSize(36)
                loserMSG.draw(gwin)
                
            elif myBlackJack.evaluteHand(dHand) == myBlackJack.evaluteHand(pHand) and myBlackJack.evaluteHand(dHand)<=21:
                loserMSG = Text(Point(310,300),'THIS ROUND WAS A TIE!')
                loserMSG.setFill('red')
                loserMSG.setSize(36)
                loserMSG.draw(gwin)

            elif myBlackJack.evaluteHand(dHand) > 21:
                winnerMSG = Text(Point(310,300),'DEALER BUSTS. YOU WIN!')
                winnerMSG.setFill('blue')
                winnerMSG.setSize(27)
                winnerMSG.draw(gwin)


        #if the hit button is clicked....
        elif hitButton.clicked(pt) == True:

            #deals a card to the player and evalutate the hand total
            myBlackJack.hit(gwin,xPosP,400)
            pScore2.setText(myBlackJack.evaluteHand(pHand))
            
            #new x position created to place cards in new x positions
            xPosP = xPosP + 75

            #if dealt card gets you over 21, game over 
            if myBlackJack.evaluteHand(pHand) > 21: 
                standButton.deactivate()
                hitButton.deactivate()
                message = Text(Point(300,300),"You busted")
                message.setFill('red')
                message.setSize(36)
                message.draw(gwin)
                
        #if new game is clicked, all is erased and blackjack function is called again
        elif newgameButton.clicked(pt)==True:
            gwin.delete('all')
            dScore2,pScore2,xPosP,pHand,dHand,newgameButton,hitButton,standButton,exitButton, myBlackJack = BlackJackSetup(gwin)

        #if none of the buttons are click then just return mouse click positions
        pt = gwin.getMouse()
        
    #window closes when the exit button is clicked
    gwin.close() 

def main():
    
    #draws a graphic window
    gwin = GraphWin("Black Jack", 600,600)

    #create background
    background = Image(Point(300,300),'splashscreen.gif')    
    background.draw(gwin)

    greeting = Text(Point(300,500),"Let's Play A Game Of BlackJack!\n Click anywhere to continue!")
    greeting.setSize(30)
    greeting.setFill('white')
    greeting.draw(gwin)

    pt = gwin.getMouse()
    greeting.undraw()
  
    
    #begins the blackjack game which calls on blackjack classes
    BlackJackGame(gwin)

main()
    
    
    
