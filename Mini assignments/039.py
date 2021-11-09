from random import randint

num = randint(1, 10)
guesses = 0

guess = int(input("Guess a number between 1 and 10.\nYou have three guesses:\n "))

if (guess != num):
    guesses += 1
    
    guess2 = int(input("Guess again: "))

    if (guess2 != num):
        guesses += 1

        guess3 = int(input("Guess again: "))

        if (guess3 != num):
            guesses += 1
            print(f"Wrong number! The correct number was {num}")
            print(f"It took you {guesses} guesses")
        else: 
            print(f"Correct! The number was {num}")
            print(f"It took you {guesses} guesses")
    else: 
        print(f"Correct! The number was {num}")
        print(f"It took you {guesses} guesses")
else: 
    print(f"Correct! The number was {num}")
    print(f"It took you {guesses} guesses")