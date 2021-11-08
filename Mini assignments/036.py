type = input("Enter the type measurement (F or C) ")
temp = int(input(f"Degree in {type} "))

if (type == "F"):
    if (temp <= 32):
        print("Freezing")
    elif (temp > 212):
        print("Boiling")
    else:
        print("Liquid")

if (type == "C"):
    if (temp <= 0):
        print("Freezing")
    elif (temp > 100):
        print("Boiling")
    else:
        print("Liquid")
