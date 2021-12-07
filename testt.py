import re

coolStr = "Hello World"

toReplace = input("What would you like to replace l with")

print(coolStr.replace("l", toReplace))

print(re.sub(r'l', toReplace, coolStr))