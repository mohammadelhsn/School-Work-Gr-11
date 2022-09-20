############################################################################# #Author: Mohammad El-Hassan #Description: Jumble [Challenging] #Date Created: 2021/11/25 #Date Modified: 2021/11/29 #############################################################################
from time import sleep as s;bottles = int(input("How many bottles of beer are on the wall? "))
while (bottles > 0): # while loop to loop 
    if (bottles == 1): print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.") # print statement for singular bottle
    else: print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer."); print("Take one down, pass it around") # print statement for plural 
    bottles -= 1; s(1); continue # some stuff that does stuff *hint* it does stuff 
print("No more bottles of beer on the wall, no more bottles of beer.") # no more bottles of beer!           