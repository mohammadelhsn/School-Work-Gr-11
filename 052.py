from random import randint 
import typing

outFile = open("lottery.txt", "w")

num = ""
company = ""

for i in range (3): num += f"{randint(1,9)}"
for i in range (3): company += f"{randint(1, 9)}"

outFile.write(num)
outFile.close()

print(f"Your number {num}")
print(f"Company {company}")

inFile = open("lottery.txt", "r")

num = list(inFile.readline())
match = 0
matched = []

for number in num:
    times = list(company).count(number)
    
    if (times > 0 and number not in matched): 
        if (times != num.count(number)): times -= 1
        if (number in matched): break  
        matched.append(number)
        match += times 

if (match == 0): print("You suck")
if (match == 1): print("You won a free ticket")
if (match == 2): print("You won 2.00 dollars")
if (match == 3): print("You won 10$ #GetScammed")



def test(test: str):
    print(test.capitalize())
    
test(1)