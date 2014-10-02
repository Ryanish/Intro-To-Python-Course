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

#4. Add code to input_guess that compares the entered number to secret_number and prints out an appropriate message such as "Higher", "Lower", or "Correct".
    
def input_guess(guess):
    # main game logic goes here 
     global number_range
     number_range = int(guess)
     print "Guess was", guess
    
# create frame
frame = simplegui.create_frame("Guess the number game", 250, 175)

# register event handlers for control elements and start frame
frame.add_button("Range is (0, 100", range100, 200)
frame.add_button("Range is (0, 1000", range1000, 200)
frame.add_input("input field", input_guess, 200)


#3. Add code to the function new_game that initializes a global variable secret_number to be a random number in the range [0, 100). Remember to include a global statement. Hint: look at the functions in the random module to figure out how to easily select such a random number. Note that the call to new_game() at the bottom of the template ensures that secret_number is always initialized when the program starts running.

#When discussing ranges, we will follow the standard Python convention of including the low end of the range and excluding the high end of the range, which can be expressed mathematically as [low, high). So, [0, 3) means all of the numbers starting at 0 up to, but not including 3. In other words 0, 1, and 2. We suggest using the range [0, 100) in your first implementation.

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

#5. Test your code by playing multiple games of “Guess the number” with a fixed range. At this point, you will need to re-run your program between each game (using the CodeSkulptor “Run” button).  You are also welcome to use this testing template http://www.codeskulptor.org/#examples-gtn_testing_template.py. The bottom of the template contains a sequence of calls to input_guess() for three games of "Guess the number". Uncomment each sequence of calls and check whether the output in the console matches that provided in the comments below. Note that your output doesn't have to be identical, just of a similar form.