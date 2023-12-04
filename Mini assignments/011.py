#############################################################################
#Author: Mohammad El-Hassan
#Description: This is a header
#Date Created: 2021/09/30
#Date Modified: 2021/09/30
#############################################################################

# Imports

# Constants

people = 5 
slices = 24

# Per Person

rem = slices % people
per = (slices - rem) / people

# Output to the console

print(f"I have set two variables - 'people' {people} and 'slices' {slices}")
print(f"We are using modulus and division")
print(f"There are {people} people at a party, each person will receive {round(per)} with a remainder of {rem}")