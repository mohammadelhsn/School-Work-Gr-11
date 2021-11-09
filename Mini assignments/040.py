from winsound import * 
import datetime
PlaySound("piaon.wav", SND_FILENAME)

now = datetime.datetime.now()

print(f"Date: {now.year}/{now.month}/{now.day}")
print(f"Time: {now.hour}:{now.second}:{now.microsecond}")