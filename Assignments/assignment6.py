first_name = input('Enter your first name: ')
last_name = input('Now, enter your last name! ')

full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
len_first = len(first_name)
len_last = len(last_name)
lower = f"{full_name.lower()}"
upper = f"{full_name.upper()}"
initials = f"{first_name[0]} {last_name[0]}"
sentence = f"I think that {first_name.capitalize()} is a great first name and {last_name.title()} is an even better last name! "

print(f"{full_name} you have {len_first} letter(s) in your first name and {len_last} letter(s) in your last name")
print(f"This is lower case: {lower}")
print(f"This is upper case: {upper}")
print(f"These are your initials: {initials}")
print(sentence)
