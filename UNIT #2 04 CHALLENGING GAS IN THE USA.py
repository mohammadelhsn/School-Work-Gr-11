#############################################################################
#Author: Mohammad El-Hassan
#Description: GAS IN THE USA [Challenging] 
#Date Created: 2021/11/25
#Date Modified: 2021/11/29
#############################################################################

from random import randint 

## Defining some cool variables

small_count = 0
big_count = 0
extra = 0

# Ask for user input

litres = int(input("How many litres in the gas tank? "))
extra = input("Are you filling up any extra cans? ")

if (extra.lower() == "yes"):
    small_count = int(input("How many 10L cans "))
    big_count = int(input("How many 20L "))

total_liters = litres + (small_count * 10) + (big_count * 20)

# Output total litres

print(f"Total in litres: {total_liters}")

# Calculate price in Canada 

canada_prices = [1.19, 1.12 , 1.14, 1.16, 1.21]
price_canada = canada_prices[randint(0, canada_prices.__len__() - 1)]

print(f"Price in Canada: {price_canada}")

total_cost = total_liters * price_canada

print(f"Price in Canada: {total_cost}")

######################### USA SECTION ############################## 

## Litres to gallons ##

gallons = total_liters / 3.785

## Litres to gallons ##

print(f"Gallons: {round(gallons, 2)}")

us_prices = [2.40, 2.50, 2.54, 2.60, 2.65] 
price_us = us_prices[randint(0, us_prices.__len__() - 1)]

print(f"The rate in the US: {price_us}")

total_uscost = gallons * price_us

def convert():
    exchange = 0.78340 
    return round((total_cost * exchange) + 4.75, 2)

print(f"Price in the United States {convert()}")
print(f"You saved {round(total_cost - convert(), 2)}")
