# Zadanie z lista liczb od -4 do 4
# 1) Wyswietl w konsoli nastepujace informacje z uzyciem petli na liscie
#    oraz instrukcji if elif else w celu sprawdzenia czy liczba jest parzysta
#    czy nie parzysta, oczywiscie dodaj informacje w konsoli
# 2) Pamietaj ze 0 bedzie oddzielnym przypadkiem, który musisz sprawdzic jako
#    pierwszy w if i w jej bloku napisz w konsoli tekst: "Zero jest parzyste".
#    Nastepnie w elif sprawdz czy liczba jest parzysta a oczywiscie w else
#    bedzie pewnosc ze jest nieparzysta

list = [-4,-3,-2,-1,0,1,2,3,4]

for i in list:
    if i == 0:
        print(i," : Zero jest parzyste")
    elif i % 2 == 0:
        print(i, " : to liczba parzysta")
    else:
        print(i, " : to liczba nieparzysta")