# 1. Napisz funkcje findLargest która przyjmuje
#    dwie liczby jako parametry num1 i num2.
#    Funkcja musi pokazac w konsoli informacje,
#    ktora liczba jest wieksza oraz jej wartosc.
#    np: "num1 jest wieksza liczba: 12" lub, ze obie
#    liczby sa rowne.
#    Pamietaj aby uzyc if elif oraz else.
# 2. Dodatkowo funkcja zwraca wieksza liczbe dzieki return
# 3. Sprawdz funkcje przekazujac wartosci 3 i 10,
#    pokaz w konsoli zwrocona wartosc z funkcji
# 4. W ten sam sposób sprawdz funkcje dla 12 i 7


def findLargest(num1, num2) :
    if (num1 > num2) :
        print ("num1 jest wieksze:", num1)
        return num1
    elif (num2 > num1):
        print ("num2 jest wieksze", num2)
        return num2
    else:
        print("Obie liczby sa równe o wartosci:", num1)
        return num1
    
v1 = findLargest (10, 10)
print ("Wynik wywolania:", v1)

v2 = findLargest (12, 7)
print("Wynik wywolania:", v2)