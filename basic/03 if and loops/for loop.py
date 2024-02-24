
for i in [1,2,3,4]:
    print(i * 2)

for i in ("Ania", "Ola", "Rafal"):
    print(i)

for i in {3,4,5,6,"Ola"}:
    print(i)

for i in "Hello":
    print(i)
else:
    print("petla zakonczona")

dictonaryData = {"Ania": "ania@gmail.com", "Ola": "ola@gmail.com", "Kasia": "kasia@gmail.com"}

for i in dictonaryData:
    print(i)

for i in dictonaryData:
    print(dictonaryData[i])

for i,n in dictonaryData.items():
    print(i , " : " , n)

for i in dictonaryData.values():
    print(i)