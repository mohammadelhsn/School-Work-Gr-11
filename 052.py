from random import randint 

outFile = open("lottery.txt", "w")

num = ""
company = ""

for i in range(3): num += f"{randint(1, 9)}"
for i in range(3): company += f"{randint(1, 9)}"

outFile.write(num)
outFile.close()

print(num)

inFile = open("lottery.txt", "r")

num = list(inFile.readline())
match = 0
for number in num:
    matched = []
    print(company.count(number))
    if (company.count(number) == 1):
        if (len(matched) > )
        match += 1
        matched.append(number)
    
print(match) 
 