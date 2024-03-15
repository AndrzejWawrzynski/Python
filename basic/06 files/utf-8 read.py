import os

scriptData = os.path.dirname(__file__)

fh = open(scriptData + "/ogonki.txt", "r", encoding="utf-8")
lines = fh.readlines()
fh.close()

# print(lines)
for l in lines:
    print(l)

fh = open(scriptData + "/ogonki.txt", "r", encoding="utf-8")
print("\n")

while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()