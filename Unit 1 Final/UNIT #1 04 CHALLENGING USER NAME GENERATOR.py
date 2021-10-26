#############################################################################
#Author: Mohammad El-Hassan
#Description: UNIT #1 04 CHALLENGING USER NAME GENERATOR
#Date Created: 2021/10/26
#Date Modified: 2021/10/26
#############################################################################

# Ask user for input

name = input("Enter your name (must be longer than 4 chars) ")
print("❌ | False" if len(name) < 4 else "✅ | True")
last_name = input("Enter your last name ")
print(f"The last letter in your last name is {last_name[len(last_name)-1]}")
age = int(input("Enter your age "))
month_born = input("Enter the month you were born in (Ex: June) ")

# Calculations and vars

len_first = len(name)
len_last = len(last_name)
first_letter = name[0]
last_letter = last_name[len(last_name)-1]
letter_month = month_born[0]
calc = len_first + len_last + age
print(calc)
pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
index = pi[calc]
new_user = f'{first_letter}{last_name.lower()}{letter_month}{index}{len(month_born)}{last_letter}@compsci.ca'

# Output data

print(f"First 100 digits of Pi: {pi}")
print(f"The length of your first name is: {len_first}")
print(f"The length of your last name is: {len_last}")
print(f"Age: {age}")
print(f"Your first ininitial in your first name is: {first_letter}")
print(f"The first initial in your birth month is: {letter_month}")
print(f"I have added the lengths of your 1) first name plus  2) last name 3) plus your age and got: {calc}")
print(f"I have counted {calc} spaces in pi to get the number {index}")
print(f"Your new username is: {new_user}")