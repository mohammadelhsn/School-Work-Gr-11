letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

sentence = input("Enter a sentence: ")
sentence = sentence.split(" ")

print("Original sentence: ", sentence)

new_list = []
words = []

for word in sentence:
    print(word)
    for letter in word:
        if (letter == " "): continue
        letter_index = letters.index(letter) + 3
        if (letter_index > 25): letter_index -= 25
        new_list.append(letters[letter_index])

for word in list(sentence):
    new_word = "".join(new_list[0:len(word)])
    del new_list[0:len(word)]
    words.append(new_word)

print(" ".join(words))