# Zadanie na Number:
# 1) pobierz liczbe calkowita od uzytkownika do zmiennej
#    za pomoca funkcji input, przekaz do niej informacje: Podaj liczbe calkowita.
# 2) Zmien typ wartosci z tekstu na liczbe calkowita
# 3) Stworz funkcje calculateSquareArea z parametrem height
#    która zwraca powierzchnie kwadratu.
# 4) Wywolaj funkcje z wczesniej pobrana liczba catkowita,
#    wynik pokaz w konsoli.
# 5) Pobierz od uzytkownika liczbe dziesietna, pamietaj o kropce
#    w liczbie. Oblicz powierzchnie kwadratu z ta wartoscia,
#    pokaz wynik w konsoli zaokraglony do 2 miejsc po przecinku.

numberInt = int(input("Podaj liczbe calkowita : "))

def calculateSquareArea(height):
    return height ** 2

print("Powierzchnia kwadratu o boku :", numberInt, "to", calculateSquareArea(numberInt))

numberFloat = float(input("Podaj liczbe dziesietna : "))

print("Powierzchnia kwadratu o boku :", numberFloat, "to", round(calculateSquareArea(numberFloat), 2))