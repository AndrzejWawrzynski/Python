
fh = open("text.txt", "r")
lines = fh.readlines()
fh.close()

for l in lines:
    print(l)