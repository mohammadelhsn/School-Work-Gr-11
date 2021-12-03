ask1 = int(input("First number "))
ask2 = int(input("Second number "))

list1 = [ask1]
total = 0

while True: 
    nextNum = list1[-1] + 1
    total += nextNum
    if (nextNum == ask2):
        list1.append(nextNum)
        break
    else: 
        list1.append(nextNum)
        
print(total)
print(list1)
print(sum(list1))