#############################################################################
#Author: Mohammad El-Hassan
#Description: This is a header
#Date Created: 2021/09/30
#Date Modified: 2021/09/30
#############################################################################

price = float(input("Price of item: $"))
tax = round(price * 0.13, 2)
total = round(price + tax, 2)

print(f"Tax: ${tax} and Total price is ${total}")