# 1. Wykorzystaj funkcje input() wbudowana w python do
#    pobrania informacji od uzytkownika z konsoli.
#    Popros uzytkownika o podanie imienia, nazwiska, miasta
#    Zapisz te informacje w zmiennych name, surname i city
# 2. Wyswieti w konsoli tekst podsumowujacy pobrane dane:
#    "Nazywasz sie Ania Kowalska i mieszkasz w miescie: Krk"

print("Podaj swoje imie")
name = input()

print("Podaj swoje nazwisko")
surname = input()

print("Podaj miejsce zamieszkania")
city = input()

print("Nazywasz sie " + name + " " + surname + " i mieszkasz w miejcowosci " + city)
print("Nazywasz sie", name, surname, "i mieszkasz w miejcowosci", city)