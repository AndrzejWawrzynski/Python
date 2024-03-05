# Zadanie - zarzadzanie ksiazka adresowa
# W tym zadaniu bedziesz uzywac stownikow do zarzadzania prosta
# ksiazka adresowa. Nauczysz sie dodawac, usuwac, kopiowac oraz
# przeszukiwac dane w slowniku.
# 1) Stworz slownik 'addressBook' zawierajacy poczatkowo jedna
#    osobe: Jan Kowalski, mieszka w Gdansku, kod pocztowy 80-000.
# 2) Dodaj do ksiazki adresowej nowa osobe: Anna Nowak, mieszka w
#    Warszawie, kod pocztowy 00-001.
# 3) Usun Jan Kowalski z ksiazki adresowej.
# 4) Skopiuj ksiazke adresowa do nowej zmiennej i sprawdz, czy
#    kopia jest identyczna (porownaj reference i zawartosc).
# 5) Sprawdz, czy w skopiowanej ksiazce adresowej jest osoba
#    mieszka w Krakowie. Jesli nie, wyswietl odpowiedni komunikat.
# 6) Wyswietl wszystkie klucze i wartosci w ksiazce adresowej.
#

addressBook = {
    "Jan Kowalski":{"city": "Gdansk", "postalCode" : "80-000"}
    }

addressBook["Anna Kowalska"] = {
    "city": "Warszawa", "postalCode" : "00-001"
}
print(addressBook)
del addressBook["Jan Kowalski"]
print(addressBook)
addressBookCopy = addressBook.copy()

print(addressBook["Anna Kowalska"] is addressBookCopy["Anna Kowalska"])
print( addressBook == addressBookCopy)
print( addressBook is addressBookCopy)

for person in addressBookCopy.values():
    if person["city"] == "Krakow":
        print("Mieszka w Krakowie")
    else:
        print("Nie mieszka w Krakowie")

found = False
for person in addressBook.values():
    if person["city"] == "Kraków" :
        found = True
    print("W ksiazce adresowej jest osoba z Krakowa")

if not found:
    print("W ksiazce adresowej nie ma osoby z Krakowa")

print("klucze :" , addressBook.keys())
print("wartosci :" , addressBook.values())
