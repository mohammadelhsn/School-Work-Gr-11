#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignement #8
#Date Created: 2021/10/15
#Date Modified: 2021/10/15
#############################################################################

import math

# Ask for user input
width = input("Enter width (measurement in feet) ")
inches1 = input('Enter inches ')
length = input("Enter length (measurement in feet) ") 
inches2 = input('Enter inches ')

# Convert to inches than add all the inches together than divide by 144 to get thee 
# square feet

square_feet = (float(width) * 12 + int(inches1)) * (float(length) * 12 + int(inches2)) / 144
boxes = (square_feet / 18.31)
print(boxes)
# Round up because if you need 5.4 boxes you will need to buy 6

total_boxes = int(math.ceil(boxes) + 1)

# Cost * total boxes 

total_cost = 50.90 * total_boxes

print(f"Floor is {round(square_feet, 2)}ft\u00b2")
print(f"You will need {total_boxes} (including the required extra box!)")
print(f"Your total cost will be ${round(total_cost, 2)}")