# Zadanie: Rezerwacja biletow na koncert
#
# Cel: Napisz program, ktory pozwoli uzytkownikowi zarezerwowac bilety na koncert.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcje bookTickets, ktora przyjmuje nazwe zespolu jako argument
#    pozycyjny (band), liczbe biletow jako argument pozycyjny, a rodzaj biletow i sekcje
#    jako argumenty nazwane z domysnymi wartosciami jako standard i general
# 2) Funkcja powinna wyswietlac informacje o rezerwacji, wlaczajac w to wszystkie
#    podane detale.
# 3) Popros uzytkownika o wprowadzenie nazwy zespolu i liczby bieltow,
#    nastepnie tylko je przekaz przy wywotaniu funkcji.
#

def bookTickets(band, numbersTickets, / , * , typeTickets = "standard", sections = "general"):
    print("Rrezerwacja " + str(numbersTickets) + " biletow na koncert zespolu " + band)
    print("Rodzaj biletu : " + str(typeTickets))
    print("Sekcje : " + sections)

band = input("Podaj nazwe zespolu :")
numbersTickets = int(input("Podaj ilosc biletow :"))

bookTickets(band, numbersTickets)