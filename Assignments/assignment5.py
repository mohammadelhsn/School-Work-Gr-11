###
# You can use comparison operators to compare two values. In functions if you have an 
# optional argument or parameter, you need to be able to find out if the argument has been
# passed or not. If not assign a default value with assignment operators.
# Arithmetic  operators are used to perform arithmetic  operations on two values. For 
# example, in one of my past projects I used arithmetic operators to keep track of the
# total times someone has used a command for stats. The only way to do this is by fetching 
# last number and add one to it.
#
# Arithmetic is also used in video games developement, usually used to add a certain 
# amount of points to a score. 
###


# In this example if b is not passed then it will be equal to a and then add them together 
# main(5): Returns 10
#
# If B is passed it it will simply print the sum of the two numbers. 
# main(5, 6): Returns: 8


def main(a, b=None):
    if a and b:
        print(a + b)
    elif a:
        b = a
        a += b
        print(a)

main(4)

main(5, 6)
