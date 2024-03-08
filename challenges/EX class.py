# Zadanie - zarzadzanie kontem uzytkownika
# W tym zadaniu stworzysz prosta klase reprezentujaca konto uzytkownika.
# Bedziesz zarzadzac podstawowymi informacjami o uzytkowniku oraz umozliwic zmiane hasla.
# 1) Stworz klase User, kóra w konstruktorze przyjmuje dwa parametry:
#    username (nazwa uzytkownika) i password (hasto). Zapisz te wartosci jako atrybuty obiektu.
# 2) Dodaj metode changePassword, która przymuje dwa argumenty:
#    oldPassword (stare hasto) i newPassword (nowe hasto). Sprawdz, czy stare haslo
#    zgadza sie z obecnym haslem uzytkownika. Jesli tak, zmien haslo na nowe.
# 3) Stworz instancje klasy User z przykladowym uzytkownikiem.
# 4) Sprobuj zmienic haslo uzytkownika za pomoca metody changePassword.
#    Najpierw uzyl nieprawidlowego starego hasla, a nastepnie prawidlowego.


class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.printInfo()


    def printInfo(self):
        print("user :", self.username, "||" , "password :", self.password)


    def changePassword(self, oldPassword, newPassword):
        if self.password == oldPassword:
            self.password = newPassword
            print("Haslo zostalo zmienione")
        else:
            print("Niepoprawne haslo")

user1 = User("Adam", "1234567890")
user1.changePassword("enjienine","iunvuibevuibcw")
user1.changePassword("1234567890","0987654321")
user1.printInfo()


