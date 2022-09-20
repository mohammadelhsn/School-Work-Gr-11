#############################################################################
#Author: Mohammad El-Hassan
#Description: Jumble [Challenging] 
#Date Created: 2021/11/25
#Date Modified: 2021/11/29
#############################################################################

from random import randint, shuffle

# Define a function that way we can use the 'return' keyword 
# to exit the program instead of having to use a break statement
# or a bunch of guard clauses.

def main():
    # Define an a̶r̶r̶a̶y̶ list of words
    
    words = ["able", "zone", "were", "user", "sold", "sake", "plus", "menu", "home", "farm"]
    
    # Get a random word from the list
    
    word =  words[randint(0, len(words) - 1)]
    
    # Save the word in another variable so it doesn't get overriten when shuffled
    
    correct = word

    word = list(word.lower())

    # 🔀 Shuffle the letters in the word

    shuffle(word)
    
    shuffled = "".join(word)
    
    # Define a list and join to form the word
        
    """
    I was going to originally doing this with a bunch of ternary operators
    but, I got lazy and decided to just use a list instead 👍
    """    
        
    guesses = []
    guess_count = 0
    # shuffle the word and display it to the user

    print(f"Your scrambled word is {shuffled}")

    print(f"Start making your guesses now: ____")

    # define this handy function to do word guessing after the 
    # user has guessed a letter

    def guess_word(guess):
        # str.strip() removes all whitespace, 
        # ⚠️ REMEMBER TO SAVE IT IN A NEW VARIABLE OTHERWISE IT WON'T WORK!!! ⚠️
        
        better_word = guess.strip()
        if (better_word == correct):
            print("✅ | You got it!")
            return True
        else: return False

    # Guess #1

    guess = input("Guess the first letter ")
    
    # If guess is correct, replace the first underscore with the letter
    # If guess is incorrect, leave it the way it is
    
    if (guess == correct[0]):
        print("✅ | Correct")
        guesses.append(correct[0])
        print("".join(guesses) + "?" * (4 - len(guesses)))
    else: 
        print("❌ | You got the letter wrong!")
        guesses.append("?")
        print("".join(guesses) + "?" * (4 - len(guesses)))
        
    if (guess_word(input("What is your guess for the word? "))):
        return 
    else: print("❌ | Wrong!")
    
    guess1 = input("Guess the second letter: ")

    # If guess is correct, replace the second underscore with the letter
    # If guess is incorrect, leave it the way it is

    if (guess1 == correct[1]):
        print("✅ | Correct")
        guesses.append(correct[1])
        print("".join(guesses) + "?" * (4 - len(guesses)))
    else: 
        print("❌ | You got the letter wrong!")
        guesses.append("?")
        print("".join(guesses) + "?" * (4 - len(guesses)))

    if (guess_word(input("What is your guess for the word? "))):
        return 
    else: print("❌ | Wrong!")
        

    guess2 = input("Guess the third letter: ")

    # If guess is correct, replace the third underscore with the letter
    # If guess is incorrect, leave it the way it is

    if (guess2 == correct[2]):
        print("✅ | Correct")
        guesses.append(correct[2])
        print("".join(guesses) + "?" * (4 - len(guesses)))
    else: 
        print("❌ | You got the letter wrong!")
        guesses.append("?")
        print("".join(guesses) + "?" * (4 - len(guesses)))

    if (guess_word(input("What is your guess for the word? "))):
        return
    else: print("❌ | Wrong!")
main()



