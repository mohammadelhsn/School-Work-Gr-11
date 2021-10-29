def getTotal(nums):
    total = 0
    for i in nums:
        total += i
    return total

def printTotal(total):
    print(f"TOTAL: {total}")

def makeChoice(choice1, choice2):
    choice = int(input(f"Enter 1 for {choice1} or 2 for {choice2}: "))

    while choice != 1 and choice != 2:
        choice = int(input(f"Enter 1 for {choice1} or 2 for {choice2}: "))
    return choice

cpus = [ 400, 100 ]
ram = [ 200,  80 ]
mobo = [300, 80]
gpu = [700, 350]

budget = int(input("Enter your budget: "))

total = []

cpu_choice = makeChoice("Ryzen 7 3700x [$400]", "Intel Core i3-7100 [$100]") - 1
total.append(cpus[cpu_choice])
printTotal(getTotal(total))
ram_choice = makeChoice("Corsair Vengance 16 GB DDR4 [$200]", "Adata 8 GB DDR3 [$80]") - 1
total.append(ram[ram_choice])
printTotal(getTotal(total))
mobo_choice = makeChoice("Gigabyte Aorus Master [$300]", "Asus B250M-C [$80]") - 1
total.append(mobo[mobo_choice])
printTotal(getTotal(total))
gpu_choice = makeChoice("Gigabyte RTX 2060 Super [$700]", "Gigabyte GTX 1050 Ti [$350]") - 1
total.append(gpu[gpu_choice])
total_total = getTotal(total)
printTotal(getTotal(total))

if (total_total > budget):
    print(f"You cannot afford this! You are ${abs(budget - total_total)} short")
else: 
    print("You can afford this! Now buy it!")

