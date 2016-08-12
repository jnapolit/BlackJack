
*****************************************************************************************
Author : Jessica Napolitano 
Created: 4/15/2014

Modification Date         Name                      Description   
6/7/2014		  Jessica Napoltiano 	    Updated graphics with background

*****************************************************************************************



WHAT TO RUN: 
	
	To play the game run blackjackgame.py. 



DESCRIPTION :

    	This application allows the user to play a friendly game of blackjack against the computer, which is always the dealer. It has a user interface with basic 
graphics. The game allows the user to play a new game whenever they want without having to close the applicationa and fire it back up again. It will keep track of the
score of both the computer and user and at the end will conclude the result of whether the user won, lost, or tied. 



DESCRIPION OF MAJOR CLASSES AND METHODS: 

	So the first class I created was the playing card class. In this class, I made the getRank and getSuit methods which would be utalised later. What get
rank does is basically it gets the rank of the card. The rank is the value of the card (So 2 has a rank of 2, Ace has a rank of 1, and jack has a rank of 11. It goes up to 13). 
The getSuit method similarly returns the suit of the card (So either heart, diamond, spade, clover). This class also incudes the function called BJValue which, given 
a playing card object, it will evaluate the rank of the card as used in BlackJack. Therefore all face cards will have the BJ value of 10. 

	The next class I created was the deck class. In it, I initally made a deck of cards utalizing the previous playingcard class and two for loops. I then made 3 helpful
methods that I will implement later on. The first method was the shuffled method. This method does what it says, it shuffles the list of cards that I just created. The 
next method was called dealcard. This pops a card from the the deck and returns it as long as the deck is not empty. The final method, cardLeft, just returns however many cards
are left in the deck. 

	The next class I created was called the buttonclass. This class consists of methods called: deactivate, activate, getlabel, and clicked. The activate and deactivate
do what they say. They allow the button to be clicked if it is active and if it is not activate, it changes the color to a more light gray and makes it so that the user
cannot click it. Getlabel simply returns the label of the button and clicked returns either True, you clicked it or False, you did not click it. 

	The next class I made was the blackjackclass which implements function that will be used in the game such as inital deal which initally deals the first two cards 
to both the computer and player, hit which will give another card to the player (note this function is only for the player), and evalute hand which given a hand will 
determine it's total BJ value (note this function takes into account whether an Ace should be counted as a 1 or 11, and DealerPlays simulates the moves the computer 
will do as the dealer, so as long as it is under 17, it will continue to hit. 

	All of these classed culminated inside the main function called blackjackgame which in itself is completely commmented so that it is easier to follow... 


WAYS TO IMPROVE: 
	
	In the future I hope to add in betting so that both the player and computer can make bets on their moves. In addition, I hope to account for more BlackJack
rules such as splitting and doubling down. 

