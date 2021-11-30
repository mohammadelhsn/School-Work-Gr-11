from random import * 


escaped = False

while escaped == False:
    user = input("You are trapped, what do you do? ")
    
    words = user.split(" ")
    
    if (words[0] == "open" and words[1] == "door"):
        print("You open the door and escape!")
        escaped = True
    elif (words[0] == "open" and words[1] != "door"):
        print("The word 'open' is correct")
    elif (words[0] != "open" and words[1] == "door"):
        print("The word 'door' is correct GG")
    else: 
        print("None of the words are correct")