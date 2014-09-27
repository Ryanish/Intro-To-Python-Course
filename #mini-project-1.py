# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# Author: Ryanish

# --------------------------------------------

# imported math function:
from random import randrange

# helper functions:

# convert name to number using if/elif/else
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "That is not an option - try again"

 # convert number to a name using if/elif/else
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "That is not an option - try again"

def rpsls(player_choice):
# print out the message for the player's choice
    print "Player chooses " + player_choice
# convert the player's choice to player_number using the function name_to_number()
    name_to_number(player_choice)
# compute random guess for comp_number using random.randrange()
    comp_number = randrange(0, 5)
# convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
# print out the message for computer's choice
    print "Computer chooses " + comp_choice
# compute difference of comp_number and player_number modulo five
    difference = (name_to_number(player_choice) - comp_number) % 5
# use if/elif/else to determine winner, print winner message - including the line break for the next set of messages
    if difference == 0:
        print "Player and computer tie! \n"
    elif difference == 1 or difference == 2:
        print "Player wins! \n"
    else:
        print "Computer wins! \n"

# testing my code:
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")    

