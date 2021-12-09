import time 

name = input("What is your name? ")

toPrint = ""

total = 0 

for letter in name:
    total += 1
    time.sleep(1)
    toPrint += letter
    print(letter, end="",flush=True)

print("\nTotal", total)