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

# imported math function:

from random import randrange

# helper functions

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
    print " "
    print "Player chooses " + player_choice
    name_to_number(player_choice)
# compute random guess for comp_number using random.randrange()
    comp_number = randrange(0, 5)

# convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

# print out the message for computer's choice
    print "Computer chooses " + comp_choice
# compute difference of comp_number and player_number modulo five
    difference = (name_to_number(player_choice) - comp_number) % 5
# use if/elif/else to determine winner, print winner message
    if difference == 0:
        result = "Player and computer tie!"
    elif difference == 1 or difference == 2:
        result = "Player wins!"
    else:
        result = "Computer wins!"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")    

