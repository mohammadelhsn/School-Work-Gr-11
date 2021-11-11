from random import randint

num = randint(1,20)
guesses = 5

print(num)

correct = False

guess1 = int(input("Guess a number between 1 and 20: "))

if (guess1 == num):
    print("You guessed the number!")
else:
    print("You didn't guess the number.")
    guesses -= 1
    guess2 = int(input("Guess again: "))
    if (guess2 == num):
        print("You guessed the number!")
    else:
        print("You didn't guess the number.")
        guesses -= 1
        guess3 = int(input("Guess again: "))
        if (guess3 == num):
            print("You guessed the number!")
        else:
            print("You didn't guess the number.")
            guesses -= 1
            guess4 = int(input("Guess again: "))
            if (guess4 == num):
                print("You guessed the number!")
            else: 
                guesses -= 1  
                print("You didn't guess the number.")
                guess5 = int(input("Guess again: "))
                if (guess5 == num):
                    print("You guessed the number!")
                else:
                    print("You didn't guess the number.")
                    guesses -= 1
                    guess6 = int(input("Guess again: "))
                    if (guess6 == num):
                        print("You guessed the number!")
                    else:
                        print("You didn't guess the number.")
                        guesses -= 1
                        print("You have no more guesses.")
                        print("The number was", num)