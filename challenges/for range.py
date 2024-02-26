# Zadania z for i range
# 1) Stwórz zmienna sum, która bedzie miala ustawiona wartos 0 przed kazda petla
# 2) Zrób petle for z wartosciami od 0 do 200 z range, zsumuj liczby i wyswietl
#    rezultat w konsoli
# 3) Zrób petle for z range z liczbami od 50 do 100, dodaj je i wyswietl wynik
# 4) Zrób kolejna petle z range od 0 do 300 z krokiem co 3, dodaj liczby
#    i wyswietl wynik w konsoli

sum = 0
for i in range(201):
        sum += i
print(sum)

print("---------------")

sum = 0
for i in range(50,101):
        sum += i
print(sum)

print("---------------")

sum = 0
for i in range(0,301,3):
        sum += i
print(sum)