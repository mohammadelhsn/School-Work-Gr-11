school = input("What is the name of your school? ")

vowels = ['a', 'e', 'i', 'o', 'u']

for letter in school:
    if letter in vowels:
        print(f"Give me an {letter}!")
    else:
        print(f"Give me a {letter}!")
        
print(f"What does that spell? {school.upper()}!")
