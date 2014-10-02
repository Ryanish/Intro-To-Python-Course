# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

#initialised Globals
number_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    # remove this when you add your code    
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    pass
    
def input_guess(guess):
    # main game logic goes here	
    global = operand
    operand = int(guess) #?
    print "Guess was" + guess
    output()
    # remove this when you add your code
    pass


#Add code to the event handler input_guess(guess) that takes the input string guess, converts it to an integer, and prints out a message of the form "Guess was 37" (or whatever the guess actually was). Hint: We have shown you how to convert strings to numbers in the lectures.

    
# create frame
frame = simplegui.create_frame("Guess the number game", 250, 175)

# register event handlers for control elements and start frame
frame.add_button("Range is (0, 100" + range100 + 200)
frame.add_button("Range is (0, 1000" + range1000 + 200)
frame.add_input("input field" + input_guess + 200)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric