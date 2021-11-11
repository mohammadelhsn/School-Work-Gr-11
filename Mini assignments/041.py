def correct(missing_letters, guess):
    print("You guessed correctly!")
    missing_letters.remove(guess)

def guess_word():
    password = "secret"

    guessWord = input("Guess the word: ")
    if guessWord == password:
        print(f"Correct, the word is {password}!")
        return True
    else: 
        print(f"Wrong, the word was {password}")
        return False

def main():
    guesses = 3
    missing_letters = ["e", "r", "t"]

    guess1 = input(f"Guess a letter ({len(missing_letters)}): ")

    if guess1 in missing_letters:
        correct(missing_letters, guess1)
    else:
        print("You guessed incorrectly!")
        guesses -= 1
        
    guess2 = input(f"Guess a letter ({len(missing_letters)}): ")

    if guess2 in missing_letters:
        correct(missing_letters, guess2)
    else:
        print("You guessed incorrectly!")
        guesses -= 1

    guess3 = input(f"Guess a letter ({len(missing_letters)}): ")

    if guess3 in missing_letters:
        correct(missing_letters, guess3)

        guess_word()
    else:
        print("You guessed incorrectly!")
        guesses -= 1
        
        guess_word()

main()