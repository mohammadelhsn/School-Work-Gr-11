from random import randint 

litres = int(input("How many litres in the gas tank? "))
extra = input("Are you filling up any extra cans? ")

if (extra.lower() == "yes"):
    extra = int(input("Small can (10L) or big can (20L) "))
    small_count = int(input("How many 10L cans"))
    big_count = int(input("How many 20L"))


total_liters = litres + (small_count * 10) + (big_count * 20)

canada_prices = [1.19, 1.12 , 1.14, 1.16, 1.21]
price_canada = canada_prices[randint(0, 4)]

total_cost = total_liters * price_canada

### USA SECTION ### 

## Litres to gallons ##

gallons = total_liters / 3.785

total_cost = ""
