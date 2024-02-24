# Wyswietlenie elementow od konca z petla while
# 1) Stwórz liste elementów : Ania, Ola, Kasia, Daniel
# 2) Zapisz zmienna i od której w kazdej iteracji petli odejmiesz 1, to indeks
#    elementu w liscie. Wpisz wartosc poczatkowa jako ostatni indeks listy
#    czyli element "Daniel"
# 3) W petli while sprawdz czy i jest wieksze lub rowne zero
#    Pobierz imie z listy z uzyciem numeru indeksu w i, wyswietl je w konsoli.
#    Zmien wartosc zmiennej i

names = ["Ania", "Ola", "Kasia", "Daniel"]

i = len(names) - 1

while i >= 0:
    person = names[i]
    print(person)
    i -= 1
