#############################################################################
#Author: Mohammad El-Hassan
#Description: This is a header
#Date Created: 2021/09/30
#Date Modified: 2021/09/30
#############################################################################

age = int(input("How old are you? "))

if (age >= 16):
    print("You can drive")
else:
    print("You can't drive")

print("Drive yourself" if age >= 16 else "Get someone else to drive you")