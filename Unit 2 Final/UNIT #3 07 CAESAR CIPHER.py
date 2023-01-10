#############################################################################
#Author: Mohammad El-Hassan
#Description: Jumble [Challenging] 
#Date Created: 2021/11/25
#Date Modified: 2021/11/29
#############################################################################

# list of letters because why not

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# user input

sentence = input("Enter a sentence: ")

# convert to a list by splitting the sentence with a space 

sentence = sentence.split(" ")

# tell them the original sentence

print("Original sentence: ", sentence)

# define some lists I probably won't use lol

new_list = []
words = []

# For each word

for word in sentence:
    
    # For each letter in the word
    
    for letter in word:
        
        # If the letter is a spacebar, skip it because it's not a letter
        
        if (letter == " "): continue
        letter_index = letters.index(letter) + 3
        if (letter_index > 25): letter_index -= 25
        new_list.append(letters[letter_index])

for word in list(sentence):
    new_word = "".join(new_list[0:len(word)])
    del new_list[0:len(word)]
    words.append(new_word)

print(" ".join(words))