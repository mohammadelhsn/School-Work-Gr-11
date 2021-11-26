#############################################################################
#Author: Mohammad El-Hassan
#Description: This is a header
#Date Created: 2021/10/12
#Date Modified: 2021/10/12
#############################################################################

from random import randint, shuffle

def main():
    words = ["able", "zone", "were", "user", "sold", "sake", "plus", "menu", "home", "farm"]
    word =  words[randint(0, len(words) - 1)]
    
    correct = word

    missing_letters = []

    word = list(word.lower())

    for letter in word:
        if letter != correct[0]:
            missing_letters.append(letter)

    shuffle(word)
    word2 = "".join(word)

    print(f"Your scrambled word is {word2}")

    missing_words = '____'

    print(f"Here is your scrambled word: {missing_words}")

    def guess_word(guess):
        better_word = guess.strip()
        if (better_word == correct):
            print("You got it!")
            return True
        else: return False


    guess = input("Guess the first letter ")
    guess0_correct = False
    
    if (guess == correct[0]):
        print("Correct")
        print(f"{correct[0]}___")
        guess0_correct = True
    else: 
        print("You got the letter wrong!")
        print("____")
        

    guess1 = input("Guess the second letter ")

    guess1_correct = False

    if (guess1 == correct[1]):
        print("Correct")
        word_first = correct[0] if guess0_correct else "_"
        print(f"{word_first}{correct[1]}__")
        guess1_correct = True
    else: 
        print("You got the letter wrong!")
        word_first = correct[0] if guess0_correct else "_"
        print(f"{word_first}___")

    if (guess_word(input("What is your guess for the word?"))):
        return 
    else: print("Wrong!")
        

    guess2 = input("Guess the third letter")
    guess2_correct = False

    if (guess2 == correct[2]):
        print("Correct")
        word_first = correct[0] if guess0_correct else "_"
        word2 = correct[1] if guess1_correct else "_"
        print(f"{word_first}{word2}{correct[2]}_")
        guess2_correct = True
    else: 
        print("You got the letter wrong!")
        word_first = correct[0] if guess0_correct else "_"
        word2 = correct[1] if guess1_correct else "_"
        print(f"{word_first}{word2}__")

    if (guess_word(input("What is your guess for the word?"))):
        return
    else: print("Wrong!")
        

    guess3 = input("Guess the last letter ")

    if (guess3 == correct[3]):
        print("Correct")
        word_first = correct[0] if guess0_correct else "_"
        word1 = correct[1] if guess1_correct else "_"
        word2 = correct[2] if guess2_correct else "_"
        print(f"{word_first}{word1}{word2}{correct[-1]}")
    else: 
        print("You got the letter wrong!")
        word_first = correct[0] if guess0_correct else "_"
        word1 = correct[1] if guess1_correct else "_"
        word2 = correct[2] if guess1_correct else "_"
        print(f"{word_first}{word1}{word2}_")
        
    if (guess_word(input("What is your guess for the word?"))):
        return
    else: print("Wrong!")
        
        
main()