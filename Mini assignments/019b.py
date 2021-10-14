# Defining my cool variables

strawberries = 4.98
apples = 3.99
kiwis = 7.45
seperator = "_________________"
empty = "\n"
subtotal = strawberries + apples + kiwis
tax = (subtotal) * 0.13
total = subtotal + tax

# Making a formatting function because I'm lazy 

def formatString(price, name):
    return f"${price} {name}"

# Output the results to the terminal with a print statement

print("RECEIPT")
print(empty)
print(seperator)
print(formatString(strawberries, "strawberries"))
print(formatString(apples, "apples"))
print(formatString(kiwis, "kiwis"))
print(empty)
print(seperator)
print(formatString(subtotal, "subtotal"))
print(formatString(round(tax,2), "tax"))
print(empty)
print(seperator)
print(formatString(round(total, 2), "total"))

