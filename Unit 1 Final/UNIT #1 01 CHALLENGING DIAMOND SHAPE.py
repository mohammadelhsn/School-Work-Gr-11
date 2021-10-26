#############################################################################
#Author: Mohammad El-Hassan
#Description: UNIT #1 01 CHALLENGING DIAMOND SHAPE
#Date Created: 2021/10/26
#Date Modified: 2021/10/26
#############################################################################

# Ask user for input

char1 = input("What is the character for the outside?")
char2 = input("What is the character for the inside?")  
char3 = input("What is the character for the middle?")

# Output the result as a diamond

print("   " + char1)
print("  " + char1 + char2 + char1)
print(" " + char1 + char2 * 3 + char1)
print(char1 + char2 * 2 + char3 + char2 * 2 + char1)
print(" " + char1 + char2 * 3 + char1)
print("  " + char1 + char2 + char1)
print("   " + char1)

