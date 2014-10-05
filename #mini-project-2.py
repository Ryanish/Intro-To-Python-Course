# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# Author: Ryanish

# Begin:

import simplegui, random

#initialise global variables
number_range = 0
secret_number = 0
attempts_allowed = 0

# defined function to start and restart the game
def new_game():
    pass

# event handler functions
def range100():
    # this function changes the range to [0,100) and starts a new game
    # setting the global variables and their values
    global number_range, secret_number, attempts_allowed
    number_range = (0, 101)
    secret_number = random.randrange(0, 101)
    attempts_allowed = 7
    # print the initial game text to the player
    print "New game. Range is from 0 to 100."

def range1000():
    # this function changes the range to [0,1000) and starts a new game
    # setting the global variables and their values
    global number_range, secret_number, attempts_allowed
    number_range = (0, 1001)
    secret_number = random.randrange(0, 1001)
    attempts_allowed = 10
    # print the initial game text to the player
    print "New game. Range is from 0 to 1000."

def game_over():   
    # If the user has 0 attempts left, end the current game and start a new one of the same range
    if attempts_allowed == 0:
        print "GAME OVER - the hidden number was", str(secret_number)
        if number_range == (0, 101):
            new_game()
            range100()
        else:
            new_game()
            range1000()
    else: pass
    
def input_guess(guess):
    # setting the global variables 
    global number_range, secret_number, attempts_allowed
    # we want the users input guess string to be compared with the secret number function
    print("Your guess is " + str(guess) + ".")
    # if correct, you win
    if int(guess) == secret_number:
        print "Congrats!"
        if number_range == (0, 101):
            new_game()
            range100()
        else:
            new_game()
            range1000()
    # if incorrect, go higher and lose an attempt
    elif int(guess) < secret_number:
            print "Higher!"
            attempts_allowed -= 1
            print "You have", attempts_allowed, " attempts left!"
            game_over()
    # if incorrect, go lower and lose an attempt
    elif int(guess) > secret_number:
            print "Lower!"
            attempts_allowed -= 1
            print "You have", attempts_allowed, " attempts left!"
            game_over()
    
# create a window/frame for the game
frame = simplegui.create_frame("Guess the number game", 250, 175)

# control elements for the window/frame
frame.add_button("Number range is 0, 100", range100, 200)
frame.add_button("Number range is 0, 1000", range1000, 200)
frame.add_input("input field", input_guess, 200)

# call new_game 
new_game()
#initiate the 100 range game first so you don't need to click a button first
range100()

# End of program