# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
# import math - Will I need this?

#initialised global variables
number_range = 0
secret_number = 0

# function to start and restart the game
def new_game():
    global number_range, secret_number

# event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    # setting the global variables
    global number_range, secret_number
    number_range = (0, 101)
    secret_number = random.randrange(0, 101)
    # print the initial game text
    print "New game. Range is from 0 to 100."

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    # setting the global variables
    global number_range, secret_number
    number_range = (0, 1001)
    secret_number = random.randrange(0, 1001)
    # print the initial game text
    print "New game. Range is from 0 to 1000."
    
def input_guess(guess):
    global number_range, secret_number
    # we want the users input guess string to be compared with the secret number function
    print("Your guess is " + str(guess) + ".")
    if int(guess) == secret_number:
        print "Congrats!" 
    elif int(guess) < secret_number:
            print "Higher!"
    elif int(guess) > secret_number:
            print "Lower!"
    
# create a window/frame
frame = simplegui.create_frame("Guess the number game", 250, 175)

# control elements for the window/frame
frame.add_button("Range is (0, 100", range100, 200)
frame.add_button("Range is (0, 1000", range1000, 200)
frame.add_input("input field", input_guess, 200)

# call new_game 
new_game()
#initiate the 100 range game first so you don't need to click a button first
range100()