password = "password"

print("The length of the password is:", len(password))
guesses = 0
correct = 0

while guesses != 3:
    print(guesses)
    correct = 0
    
    guess = input("Enter the password: ")

    
    for letter in guess: 
        if (correct == 8): guesses = 3
        if (letter in password): correct += 1; print(f"{letter} is in the password")
        else: print(f"{letter} is not in the password")
    guesses += 1
if(guesses == 3 and correct == 8): 
    print("You have guessed the password correctly")
else: print("You have failed to guess the password\nLOSER")