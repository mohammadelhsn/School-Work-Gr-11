start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

def sum2(list):
    index = len(list)
    total = 0
    
    while index != 0:
        total += list[index-1]
        index -= 1
    return total

newlist = []

for i in range(start, end + 1): newlist.append(i)
    
print(sum2(newlist))