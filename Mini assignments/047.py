start = int(input("Gimme a number that isn't 0 "))
end = int(input("Gimme another number that isn't 0 "))
increment = int(input("Gimme another number that isn't 0 "))

addition = start
subtraction = end
multiplying = start
division = end

while addition != end:
    if (addition >= end): break
    addition += increment
while multiplying != end:
    if (multiplying >= end): break
    multiplying *= increment
while subtraction != start:
    if (subtraction <= start):  break
    subtraction -= increment
while division != start:
    if (division <= start): break 
    division /= increment
    
print(addition)
print(subtraction)
print(multiplying)
print(division)