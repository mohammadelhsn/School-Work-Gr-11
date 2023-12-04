#############################################################################
#Author: Mohammad El-Hassan
#Description: This is a header
#Date Created: 2021/09/30
#Date Modified: 2021/09/30
#############################################################################

# Imports

from random import randint

# Constants

rps = ["rock", "paper", "scissors"]

index = randint(0, 2)

choice = rps[index]

user_choice = input("Rock, paper or scissors? ")

if (user_choice.lower() == choice):
    print("Nice job, you guessed it!")
else:
    print(f"You lost, better luck next time!")

print(f"The correct guess was {choice}")