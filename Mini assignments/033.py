age = int(input("How old are you? "))

if (age >= 13 and age <= 15):
    print("You are in grade 9 or 10")

elif (age >= 16 and age <= 18):
    print("You are in grade 11 or 12")
elif (age < 13):
    print("Probably in elementary")
else:
    print("You are 19 or older")
