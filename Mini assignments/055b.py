import re 

letter = input("Enter a letter to replace z: ")

sentence = "Shz szlls szashZlls by the sza shorZ"

new = re.sub(r'z', letter.lower(), sentence)

print(re.sub(r'Z', letter.lower(), new))