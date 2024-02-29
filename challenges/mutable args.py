# Przekazywanie mutowalnych danych do funkcji jak slownik, zadanie:
# 1) Utworz slownik opisujacy pracownika i zapisz go w zmiennej
#    employee. Do elementow stownika dodaj:
#    name, email, rank (stopien - wpisz programmer), salary (8000)
# 2) Napisz funkcje promoteToManager, która przyjmuje parametr
#     o nazwie user, gdzie przekazany bedzie slownik.
# 3) Wewnatrz funkcji zmien wartosci elementów przekazanego
#    slownika user, podnies pensje o 50%, zmien rank
#    na manager. Dodatkowo sprawdz czy przypadkiem przekazany
#    pracownik juz jest managerem, w takim wypadku podaj w konsoli,
#    ze osoba ta juz jest managerem i wyjdz z funkcji z return.
# 4) Wywolaj funkcje promoteToManager i przekaz utworzony na poczatku
#    slownik, pokaz w konsoli czy zostal on zaktualizowany.

employee = {
    "name" : None,
    "email" : None,
    "rank" : "programmer",
    "salary" : 8000
}

def promoteToManager(user):
    if user["rank"] == "manager":
       print("Osoba jest juz menagerem")
       return
    user["rank"] = "manager"
    user["salary"] = user["salary"] * 1.5

promoteToManager(employee)    
print(employee)