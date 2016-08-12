#CREATOR: Jessica Napolitano
#FUNCTION: Creates the object of a button with methods allowing for the user
#to change the color of the button, the label, to decide whether it is clickable
#or not, as well as the function that will return the boolean as to whether the
#button has been clicked.

from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        #The max and min is helpful on these variables because it makes it even
        #more obvious that these are our boundaries and which we will use to say
        #something like while we are not clicking the button...
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active = True #this variable keeps track of whether or not the button is currently "active"

    def setFill (self,color):
        """Sets the background color of the button"""
        self.rect.setFill(color)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    
    def deactivate(self):
        "Sets this button to 'inactive'."
        ##color the text "darkgray"
        self.label.setTextColor('darkgray')
        ##set the outline to look finer/thinner
        self.rect.setWidth(1)
        ##set the boolean variable that tracks "active"-ness to False
        self.active=False
        
    
    def clicked(self, p):
        "Returns true if button active and Point p is inside"
        if((p.getX()<= self.xmax and p.getX()>= self.xmin) and\
               (p.getY()>=self.ymin and p.getY()<=self.ymax) and self.active==True):
            
            return True
        else:
            return False

    
def main():
    
    win= GraphWin('button',400,400)

    
    
    ##create two Button objects, one for "Roll Dice" and the other for "Quit"
    ##activate the Roll button
 
    exitButton = Button(win,Point(150,200),30,20,'Exit')
    rollButton = Button(win,Point(200,200),30,20,'Roll')
    rollButton.activate()


    
    ##deactivate the "Quit" button
    exitButton.deactivate()

        

    pt = win.getMouse()
    
    ##keep taking mouse clicks (in a loop) until the "Quit" button is clicked
        ##if the roll button is clicked
            ##activate the quit button
    while exitButton.clicked(pt) == False:
        if rollButton.clicked(pt) == True:
            exitButton.activate()
        pt=win.getMouse()
               
    #we reach this line of code when quit button is clicked b/c loop condition breaks
    win.close() #so close the window, ending the program
    
if __name__ == "__main__":
    main()
