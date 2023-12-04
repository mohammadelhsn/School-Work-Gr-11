#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignment 4
#Date Created: 2021/10/12
#Date Modified: 2021/10/12
#############################################################################

# Imports

# Constants

# Defining variables

strawberries = 4.98
apples = 3.99
kiwis = 7.45
separator = "_________________"
empty = "\n"
subtotal = strawberries + apples + kiwis
tax = (subtotal) * 0.13
total = subtotal + tax

# Making a formatting to make things easier.

def formatString(price, name):
    return f"${price} {name}"

# Output the results to the terminal with a print statement

print("RECEIPT")
print(empty)
print(separator)
print(formatString(strawberries, "strawberries"))
print(formatString(apples, "apples"))
print(formatString(kiwis, "kiwis"))
print(empty)
print(separator)
print(formatString(subtotal, "subtotal"))
print(formatString(round(tax,2), "tax"))
print(empty)
print(separator)
print(formatString(round(total, 2), "total"))

