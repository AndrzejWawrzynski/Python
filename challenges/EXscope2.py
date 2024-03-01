# Zadanie: Zarzadzanie stanem konta uzytkownika
#
# Cel: Napisz program do zarzadzania stanem konta uzytkownika, który pozwala na
# dodawanie i usuwanie srodkow oraz wyswietlanie aktualnego stanu konta. Program
# powinien korzystaé z globalnej zmiennej do przechowywania stanu konta oraz
# zawierac funkcje do modyfikacji tego stanu i wyswietlania go.
#
# Kroki do wykonania:
# 1) Zdefiniuj globalna zmienna accountBalance z wartoscia poczatkowa 0.
# 2) Napisz funkcje addFunds, która przyjmuje kwote do dodania do konta.
#    Funkcja ta powinna modyfikowac globalna zmienna accountBalance.
# 3) Napisz funkcje withdrawFunds, która przyjmuje kwote do wyplaty z konta.
#    Sprawdz, czy stan konta pozwala na wyplate - jesli nie, wyswietl odpowiedni komunikat.
# 4) Napisz funkcje displayBalance, która wyswietla aktualny stan konta.
# 5) Zapytaj uzytkownika w petli o dzialanie (dodanie srodkow, wyplata, wyswietlenie stanu)
#    i odpowiednio zareaguj, wywotujac odpowiednia funkcje.
#
# Rozwiazanie:

accountBalance = 0

def addFunds(income):
    global accountBalance
    accountBalance += income
    print("Dodano srodki : ", income)

def withdrawFunds(expenses):
    global accountBalance
    if expenses > accountBalance:
        print("Nie posiadasz tyle srodkow na koncie")
    else:
        accountBalance -= expenses
        print("Wyplacono srodki : ", expenses)
    
def displayBalance():
    print("Twoj stan konta to :", accountBalance)

while True:
    action = input("Wybierz dzialanie : 'dodaj' , 'wyplac' , 'stan' , 'koniec' : ").lower()
    if action == "dodaj":
        add = float(input("Podaj kwote zasilenia konta : "))
        addFunds(add)
    elif action == "wyplac":
        sub = float(input("Podaj kwote wyplaty : "))
        withdrawFunds(sub)
    elif action == "stan":
        displayBalance()
    elif action == "koniec":
        break
    else:
        print("Nieznane dzialanie")
