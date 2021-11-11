password = "secret"
password_len = len(password)

guesses = 3

print(f"Password length is {password_len}")


correct = []
wrong = []

while guesses > 0:
    print(f"Correct: {correct}")
    print(f"Wrong: {wrong}")

    guess = input("Guess a letter: ")
    
    if (password.count(guess) > 0):
        correct.append(guess)
        print("Correct!")
    else:
        wrong.append(guess)
        print("Wrong!")

    guesses -= 1


guess = input("Guess the word: ")

if (guess == password):
    print("You win!")
else:
    print("You lose!")
    print(f"The password was {password}")
    print("You must now watch this video: https://www.youtube.com/watch?v=dQw4w9WgXcQ")
