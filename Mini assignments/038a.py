from random import randint

roll1 = randint(1,6)
roll2 = randint(1,6)
roll3 = randint(1,6)
total = roll1 + roll2 + roll3

print(f"You got a {roll1}")
input("Press any key to continue")
print(f"You got a {roll2}")
input("Press any key to continue")
print(f"You got a {roll3}")
input("Press any key to continue")
print(f"The total: {total}")
