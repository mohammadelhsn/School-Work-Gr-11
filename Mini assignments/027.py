from random import randint

password = input("Enter a password ")

correct_pass = "python123"

if (password == correct_pass):
    print("Password is correct!")
else: 
    print(f"Password is incorrect. The correct password was {correct_pass}")

ranNum = randint(1, 5)
guess = int(input("Enter a number between 1 and 5 "))

if (guess == ranNum):
    print(f"You guessed it, the num was {ranNum}")
else: 
    print(f"You didn't guess it, the correct num is {ranNum}")