#mini-project 1
import random

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
     	print "This is not an option - try again"

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
        print "This is not an option - try again"


def rpsls(player_choice):
	print " "
	print "Player chooses" + player_choice
	name_to_number(player_choice)
# compute random guess for comp_number using random.randrange()
	comp_number = random.randrange(0,4)
# convert comp_number to comp_choice using the function number_to_name()
    
# print out the message for computer's choice

# compute difference of comp_number and player_number modulo five

# use if/elif/else to determine winner, print winner message

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")    
