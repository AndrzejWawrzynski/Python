# Zadanie: Tworzenie profilu uzytkownika
#
# Cel: Napisz program, który umozliwia utworzenie profilu uzytkownika w systemie.
# Program powinien prosic uzytkownika o podanie imienia, nazwiska, wieku oraz
# miasta pochodzenia. Nie wszystkie informacje sa wymagane. Uzyj funkcji z nazwanymi
# argumentami
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcje createUserProfile przyjmujaca argumenty: firstName, lastName,
#    age oraz city
# 2) Funkcja powinna zwracac stownik zawierajacy informacje o profilu uzytkownika.
# 3) Popros uzytkownika o wprowadzenie wymaganych danych.
# 4) Wywolaj funkcje createUserProfile z odpowiednimi argumentami wrowadzonymi przez
#    uzytkownika i przechowaj zwrocony slownik.
# 5) Wyswietl zwrocony profil uzytkownika.
#
# Rozwiazanie:

def createUserProfile(firstName, lastName, age, city):
    return {
        "firstName" : firstName,
        "lastName" : lastName,
        "age" : age,
        "city" : city
    }

firstName = input("Podaj imie : ")
lastName = input("Podaj nazwisko : ")
age = input("Podaj wiek : ")
city = input("Podaj miasto : ")

user = createUserProfile(firstName=firstName, lastName=lastName, age=age, city=city)

print("Imie :", user["firstName"])
print("Nazwisko :", user["lastName"])
print("Wiek :", user["age"])
print("Miasto :", user["city"])