#############################################################################
#Author: Mohammad El-Hassan
#Description: UNIT #1 03 CHALLENGING RECEIPT WITH CHANGE
#Date Created: 2021/10/26
#Date Modified: 2021/10/26
#############################################################################

# Ask user for input

item1 = input("Enter your first item? ")
item1_price = float(input("Enter the price of your first item? "))
item1_quantity = int(input("Enter the quantity of your first item? "))
item2 = input("Enter your second item? ")
item2_price = float(input("Enter the price of your second item? "))
item2_quantity = int(input("Enter the quantity of your second item? "))

# Defining our lines for the receipt

line1 = "^" * 27
line2 = "=" * 27
space = " "

# Calcuations

subtotal = item1_price * item1_quantity + item2_price * item2_quantity
tax = subtotal * 0.13
total = subtotal + tax

# Function to get the number of spaces

def getSpace(strings):
    total = 27 
    for i in strings:
        total -= len(i)
    return space * total

# Get the spaces so that they can be aligned properly

space1 = getSpace(["ITEM", "PRICE"])
space2 = getSpace([item1, str(item1_price), str(item1_quantity), "@", " ", " ", " " f'${item1_quantity * item1_price}'])
space3 = getSpace([item2, str(item2_price), str(item2_quantity), "@", " ", " ", " " f'${round(item2_quantity * item2_price, 2)}'])
space4 = getSpace(["SUBTOTAL", f'${round(subtotal, 2)}'])
space5 = getSpace(["TAXES", f'${round(tax, 2)}'])
space6 = getSpace(["TOTAL", f'${round(total, 2)}'])

# Output results

print(line1)
print("RECEIPT")
print("ITEM"+ space1 + "PRICE")
print(line2)
print(f"{item1.lower()} {item1_quantity} @ {item1_price}" + space2 + f"${item1_quantity * item1_price}")
print(f"{item2.lower()} {item2_quantity} @ {item2_price}" + space3 + f"${round(item2_quantity * item2_price, 2)}")
print(line2)
print("SUBTOTAL" + space4 + f'${round(subtotal, 2)}')
print("TAXES" + space5 + f'${round(tax, 2)}')
print(line2)
print("TOTAL" + space6 + f'${round(total, 2)}')
print(line1)
