# Zadanie: Pretwarzanie danych uzytkownikow
# Cel: Napisz program do przetwarzania danych uzytkownikow z listy.
# Kroki do wykonania:
# 1) Stwórz liste slownikow users, gdzie kazdy slownik zawiera klucze 'name' i 'age'
#    z przykladowymi danymi uzytkownikow.
# 2) Uzyj filter do wyfiltrowania uzytkownikow, którzy maja wiecej niz 18 lat.
# 3) Uzyj map do podwojenia wieku prefiltrowanych uzytkownikow.
# 4) Uzyj reduce do zsumowania wszystkich lat po przetworzeniu.
# 5) Wyswietl sume lat prefiltrowanych i przetworzonych uzytkownikow.
# Rozwiazanie:


from functools import reduce

# Przyktadowa lista uzytkowników
users = [
{'name': 'Jan', 'age': 15},
{'name': 'Anna', 'age': 25},
{'name': 'Piotr', 'age': 30},
{'name': 'Katarzyna', 'age': 22}
]

overAge = list(filter(lambda a: a["age"] > 18, users)) # ponad 18
print(overAge)

addAge = list(map(lambda a: a["age"] * 2, overAge)) # wiek razy 2
print(addAge)

totalAge = reduce(lambda x,y: x + y, addAge) # suma lat
print(totalAge)