names = ["joe", "rick", "bob", "luke"]
added = []
removed = []

user = input("Enter your name: ")

names.append(user)
added.append(user)

print(names)

def getRemoved(): 
    if len(removed) > 0:
        return removed[0]
    else: 
        return "None"

name_remove = input("Enter a name to remove: ")

if (name_remove not in names):
    print("Name not found, no changes made")
else: 
    names.remove(name_remove)
    removed.append(name_remove.lower())
    print(names)


print(f"The following names were added: {added[0]}")
print(f"The following names were removed: {getRemoved()}")
print(f"The following names are still in the list: {names}")
print(f"{len(names)}")
print(f"The first name in the list is {names[0]}")
print(f"The last name in the list is {names[-1]}")
