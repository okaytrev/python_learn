#import random
from random import randint

#asks user for input
playoptions = ["Rock", "Paper","Scissors"]

#randomizes computer options from playoptions
computer = playoptions[randint(0,2)]

#sets player to false for loop
player = False

#Player begins
while player == False:
    #Asks user for input
    player = input("Rock, Paper, Scissors?:")
    if player == computer:
        print("Tie! You both played ", computer)
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    #invalid input print
    else:
        print("That's not valid check your spelling!")
    #sets player back to false so the game can continue
    player = False
    computer = playoptions[randint(0,2)]

