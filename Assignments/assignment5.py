###
# You can use comparison operators to compare two values. In functions if you have an 
# optional argument or parameter, you need to be able to find out if the argument has been
# passed or not. If not assign a default value with assignment operators.
#
# Arthematic operators are used for 
#
###


# In this example if b is not passed then it will be equal to a and then add them together 
# main(5): Returns 10
#
#
# If B is passed it it will simply print the sum of the two numbers. 
# main(5, 6): Returns: 8


import random

def main(a, b=None):
    if a and b:
        print(a + b)
    elif a:
        b = a
        a += b
        print(a)

main(4)

main(5, 6)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

## arthematic 
