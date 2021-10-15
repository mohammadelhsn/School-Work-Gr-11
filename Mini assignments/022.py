price = float(input("Price of item: $"))
tax = round(price * 0.13, 2)
total = round(price + tax, 2)

print(f"Tax: ${tax} and Total price is ${total}")