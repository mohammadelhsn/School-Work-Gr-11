print("You are in a prison, figure out the password to escape"); password = "get out"
while True:
    response = input("What is the password? ")
    if (response.split(' ')[0] == password.split(" ")[0] and response.split(' ')[1] == password.split(" ")[1]): break
    else: continue
print("You escaped")