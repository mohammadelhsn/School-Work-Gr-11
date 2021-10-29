#############################################################################
#Author: Mohammad El-Hassan
#Description: This is a header
#Date Created: 2021/09/30
#Date Modified: 2021/09/30
#############################################################################


name = input("What is your name? ")

if name.lower() == "mohammad":
    print("Hello, Mohammad!")
elif name.lower() == "joe":
    print('joe mama')
else: 
    print(f"Hello {name.lower().capitalize()}!")
