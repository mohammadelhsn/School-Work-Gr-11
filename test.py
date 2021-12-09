answer = "supper"

guess = "p"

num = answer.count(guess)

indexes = []

def duplicates(lst, item):
   return [i for i, x in enumerate(lst) if x == item]

print(duplicates(answer,guess))


print(enumerate(answer))