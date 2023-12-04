#############################################################################
#Author: Mohammad El-Hassan
#Description: This is a header
#Date Created: 2021/09/30
#Date Modified: 2021/09/30
#############################################################################

# Imports

from random import randint 

# Constants

bool1 = bool(randint(0, 1))
bool2 = bool(randint(0, 1))

if (bool1 == True and bool2 == True):
    print("True")
else: 
    print("False")