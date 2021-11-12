import random

sentence = input("Enter a sentence: ")

words = sentence.split()

new_words = []

for word in words: 
    if len(word) < 3:
        print(f"Word '{word}' needs to be at least 3")
    else: 
        word = list(word.lower())
        random.shuffle(word)
        new_words.append("".join(word))
        random.shuffle(new_words)

print(" ".join(new_words))