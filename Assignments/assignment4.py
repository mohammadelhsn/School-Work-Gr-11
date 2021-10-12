#############################################################################
#Author: Mohammad El-Hassan
#Description: This is a header
#Date Created: 2021/10/12
#Date Modified: 2021/10/12
#############################################################################


gift_price = 120.12
discount = gift_price * 0.2
after_discount = gift_price - discount
taxes = after_discount * 0.13
after_tax = after_discount + taxes
rem = after_tax % 4
per_person = (after_tax - rem) / 4

print("Remember every number is a variable")
print("Every calculation are using these variables")
print("Include proper spacing and $ signs")
print("You may round the number if you know how\n") # I know how
print(f"The price of the gift is ${gift_price}")
print(f"The discount to be taken off of the price is ${round(discount, 2)}")
print(f"The price after the discount is ${round(after_discount, 2)}")
print(f"The amount of taxes that need to be paid is ${round(taxes, 2)}")
print(f"The final price after taxes are added ${round(after_tax, 2)}")
print(f"Price for each person is ${per_person}")
print(f"The remainder is ${round(rem, 2)}")
