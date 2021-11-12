sentence1 = input("Enter a sentence (ending with ly): ").split()[-1]
sentence2 = input("Enter a sentence (ending with ed): ").split()[-1]

last = sentence1[-2:]

if ("ly" in sentence1[-2:]):
    print(f"The last two letters of {sentence1} is ly")
else:    
    print(f"The last two letters of {sentence1} is not ly. You entered {last}")

if ("ed" in sentence2[-2:]):
    print(f"The last two letters of {sentence2} is ed")
else:
    print(f"The last two letters of {sentence1} is not ed. You entered {last}")

