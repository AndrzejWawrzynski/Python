# Zadanie: Obliczanie pola powierzchni prostokata
#
# Cel: Napisz program, który oblicza pole powierzchni prostokata. Program
# powinien prosic uzytkownika o wrowadzenie dugosci i szerokosci prostokata,
# a nastepnie obliczy jego pole powierzchni.
# Kroki do wykonania:
# 1) Zdefiniuj funkcje calculateArea, która przyjmuje dwa parametry: length i width.
#    Funkcja ta powinna obliczac pole powierzchni prostokata i zwracac wynik.
# 2) Popros uzytkownika o prowadzenie dugosci prostokata.
# 3) Popros uzytkownika o prowadzenie szerokosci prostokata.
# 4) Wywotaj funkcje calculateArea z wrowadzonymi wartosciami i przechowaj wynik.
# 5) Wyswietl wynik obliczen uzytkownikowi.

def calculateArea(length, width):
    return length * width

num1 = int(input("Podaj dlugosc prostokata w cm: "))
num2 = int(input("Podaj szerokosc prostokata w cm: "))

areaRectangle = calculateArea(num1, num2)

print("Pole powierzchni prostokata to :" , areaRectangle, "cm2")
