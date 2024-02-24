# Skorzystaj z petli while aby dodac wartosci od 1 do 100
# 1) Dodaj zmienna i rowna 0, która bedzie inkrementowana w petli o 1.
#    Kolejna zmienna bedzie sum z wartoscia poczatkowa 0
# 2) W petli while sprawdz czy i jest mniejsze równe 100
#    Wewnatrz petli dodaj do sum wartosc i, nastepnie
#    zrób inkrementacje i o jeden
# 3) Dodaj else po petli while z tekstem w konsoli "Koniec petli while"
# 4) Zapisz podsumowanie "Suma wartosci:" oraz wynik sumy

i = 0
sum = 0

while i <= 100:
    sum += i
    i += 1
else:
    print("Koniec petli while")
print("Suma liczb o 1 do 100: ", sum)