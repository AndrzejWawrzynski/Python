# Zadanie: Kalkulator sredniej arytmetycznej
# Cel: Napisz program kalkulatora, który oblicza srednia arytmetyczna z listy liczb.
# Program powinien uzywac funkcji lambda, map oraz reduce do przetworzenia listy liczb
# i obliczenia wyniku. Zadanie ma na celu praktyczne zastosowanie wyrazen lambda
# i funkcji wyzszego rzedu do przetwarzania danych.

# Kroki do wykonania:
# 1) Zdefiniuj liste liczb, dla której ma zostac obliczona srednia arytmetyczna.
# 2) Uzyj funkcji map i lambda do przeksztalcenia listy liczb, jesli to konieczne.
# 3) Wykorzystaj funkcje reduce i lambda do obliczenia sumy wszystkich liczb z listy.
# 4) Oblicz srednia arytmetyczna dzielac sume przez ilosc liczb w liscie.
# 5) Wyswietl wynik.
# Rozwiazanie:

from functools import reduce

list = [10,20,30,40,50,60]

result = reduce (lambda x, y: x + y, list)
lenght = len(list)
avgList = round(result / lenght, 2)
print("Srednia arytmetyczna liczb z listy to :", avgList)