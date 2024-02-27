# Zadanie z zwracanym stownikiem uzytkownika
# 1) Stwórz funkcje createUser z parametrami:
#    - name
#    - contact
# 2) W ciele funkcji stworz zmienna user w której bedzie
#    slownik reprezentujacy uzytkownika. Dodaj do stownika
#    nazwe uzytkownika z parametru.
# 3) Parametr contact bedzie mogl przyjac tekst lub liczbe.
#    Sprawdz za pomoca funkcji isinstance jaki typ ma
#    przekazany parametr contact. Jezeli jest to typ string
#    to ponizszy kod zwróci wartosé True dla zmiennej contact
#    isinstance(contact, str) Wtedy zakladamy, ze jest to
#    adres email, który przypiszesz do stownika uzytkownika.
#    Natomiast jesli contact jest liczba to zakladamy, ze
#    jest to telefon, wiec zapisz element telephone
#    W zwracanym slowniku uzytkownika. Do sprawdzenia czy
#    contact jest liczba uzyj isinstance(contact, int)
# 4) Wywolaj funkcje z dwoma przypadkami:
#    - imie Ola, contact (string): ola@example.com
#    - imie Kasia, contact (number): 987654321
#    Pokaz w konsoli zwrócone stowniki.

def createUser(name,contact):
    user = {
        "name": name,
        "email": None,
        "telephone": None
    }

    if isinstance(contact, str):
        user["email"] = contact
    elif isinstance(contact, int):
        user["telephone"] = contact

    return user

user1 = createUser("Ola", "ola@example.com")
print(user1)

user2 = createUser("Kasia", 987654321)
print(user2)
    