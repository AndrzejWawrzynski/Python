#
# Funkcje String:
# 1) Napisz funkcje getUserInformation z trzema parametrami:
#    name, surname, job
# 2) W getUserInformation zmien imie i nazwisko na duze litery,
#    zawod na male, dodatkowo wyczysc te wartosci
#    z bialych znakow na ich poczatku i koncu
# 3) Polacz imie i nazwisko wraz z innym tekstem aby uzyskaé tekst np:
#    "imie: ANIA, nazwisko: KOWALSKA, zawód: testerka"
# 4) Zwroc powstaly tekst z funkcji
# 5) Wywolaj funkcje getUserInformation na nastepujacych
#    danych i pokaz wynik w konsoli:
#    - Ania, Kowalska, Programistka
#    - Daniel, Lis, Administrator

def getUserInformation(name, surname, job):
    name = name.upper().strip()
    surname = surname.upper().strip()
    job = job.lower().strip()
    text = "imie: "+ name + ", nazwisko: " + surname + ", zawod: " + job
    return text

print(getUserInformation(" \n\t Ania   ", "  Kowalska  ", "Programistka \n\t"))
print(getUserInformation("Daniel", "Lis", "   Administrator    "))
