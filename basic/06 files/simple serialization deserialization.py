import os
import pickle

scriptData = os.path.dirname(__file__)

number = 123456
list = ["ania", "ola", "kasia"]
str = "tekst ąćńłó"

fh = open(scriptData + "/data.dat", "wb")
pickle.dump(number, fh)
pickle.dump(list, fh)
pickle.dump(str, fh)

fh.close()

fh = open(scriptData + "/data.dat", "rb")
numberInfo = pickle.load(fh)
listInfo = pickle.load(fh)
strInfo = pickle.load(fh)
fh.close()

print(numberInfo)
print(listInfo)
print(strInfo)
