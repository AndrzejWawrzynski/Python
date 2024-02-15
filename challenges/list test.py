# 1. Stwórz liste data z kolejnymi liczbami: od 0 do 6
# 2. Pokaz w konsoli dlugosc listy, skasuj 2 element
#    i pokaz dlugosc listy ponownie
# 3. Uzyj instrukcji warunkowej if z in do sprawdzenia czy
#    liczba 3 jest w liscie data, pokaz informacie
#    w konsoli jesli zachodzi taka sytuacja. Przyklad:
#    if 100 in someList:
#    print("100 jest w liscie")
# 4. Uzyj petli for aby pokazac wartosci w liscie.
#    for el in someList:
#    print("element listy z dodana wartoscia 2", el + 2)
# 5. Uzyj petli for aby przejsé po elementach listy, ale
#    pokaz ich wartosci pomnozone przez 2

data = [0, 1, 2, 3, 4, 5, 6]
print("Dlugosc listy:", len(data))

del data[1]
print("Dlugosc listy po skasowaniu elementu:", len(data))

if 3 in data:
    print("3 jest w liscie data")

print("Liczby w liscie")
for i in data:
    print(i)

print("Do liczb dodano 2")
for i in data:
    newNum = i + 2
    print(newNum)  

print("Liczby pomnozone przez 2")
for n in data:
    newNum2 = n * 2
    print(newNum2)    