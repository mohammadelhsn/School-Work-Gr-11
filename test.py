num_list = []

outFile = open("num.txt", "w")

num_enter = input("Numbers(Q to quit)")

while (num_enter != "Q"):

   outFile.write(str(num_enter) + '\n')

   num_enter = input("Numbers(Q to quit)")

outFile.close()

inFile = open("num.txt", "r")

numbers = inFile.readline().rstrip()

while (numbers):

   num_list.append(numbers)

   numbers = inFile.readline().rstrip()

print(num_list)