from random import randint

rps = ["rock", "paper", "scissors"]

index = randint(0, 2)

choice = rps[index]

user_choice = input("Rock, paper or scissors? ")

if (user_choice.lower() == choice):
    print("Nice job, you guessed it!")
else:
    print(f"You lost, better luck next time!")

print(f"The correct guess was {choice}")