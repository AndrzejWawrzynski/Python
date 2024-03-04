# Zadanie - analiza danych demograficznych
# W tym zadaniu wykorzystasz krotki do przechowywania i analizy
# danych demograficznych. Uzyj podstawowych operacji na krotkach
# do manipulacji danymi oraz do wykonania prostych obliczen.
#
# 1) Stworz krotke 'population' zawierajaca liczbe ludnosci w milionach
#    dla pieciu wybranych krajow. Np. Polska - 38, Niemcy - 83 itd.
# 2) Dodaj do krotki 'population' dane dla kolejnego kraju uzywajac
#    konkatenacji.
# 3) Wyswietl dugosc krotki 'population', aby sprawdzié ile jest
#    obecnie danych.
# 4) Sprawdz, czy liczba 100 (milionów ludnosci) znajduje sie w krotce
#    population.
# 5) Wyswietl liczbe ludnosci dla trzeciego kraju w krotce.
# 6) Oblicz minimalna i maksymalna liczbe ludnosci w krotce 'population'.
# 7) Jesli maksymalna liczba ludnosci w krotce jest wieksza niz 500 mln,
#    wyswietl komunikat: "Znaleziono kraj o bardzo duzej populacji".
#    W przeciwnym razie, wyswietl: "Wszystkie kraje maja populacje ponizej 500 mln".

population = (38,83,68,59,47)
population +=(120,130)
print(len(population))

print(100 in population)

print(population[2])
print(min(population))
print(max(population))

if max(population) > 500:
    print("Znaleziono kraj o bardzo duzej populacji")
else:
    print("Wszystkie kraje maja populacje ponizej 500 mln")





