# Program ma na celu kwalifikacje kandydatow do oddania krwi
# 1) Dodaj zmienna age o wartosci 18 oraz weight = 50
# 2) Napisz instrukcje if else sprawdzajaca czy kandydat
#    ma wiek wiekszy lub rowny 18, jesli tak sprawdz kolejna
#    instrukcja if else czy jego waga jest wieksza lub równa 50.
#    Jesli oba warunki sa spelnione napisz w konsoli ze moze
#    oddac krew
# 3) W przypadku gdy jakis warunek nie jest spelniony to po else
#    napisz w konsoli daczego

age = 18
weight = 50

if age >= 18:
    if weight >=50:
        print("Moze oddac krew.")
    else:
        print("Nie moze oddac krwi, za niska waga.")
else:
    print("Nie moze oddac krwi, za maly wiek.")