# Stworz klase SimCard reprezentujaca karte sim telefonu z kontaktami
# 1) Klasa ustawia atrybut/zmienna klasy contacts jako liste w konstruktorze
# 2) Dodaj metode addContact przyjmujaca oprocz self rowniez parametry
#    name i telephone. Sprawdz z funkcja isinstance czy przekazane dane sa
#    prawidlowe, czyli str i int. Stworz slowik z name i telephone i dodaj go
#    do listy kontaktow obiektu powstalego na bazie klasy
# 3) Napisz metode showContacts, ktora w petli pokze kolejne kontakty w terminalu
# 4) Stworz instance klasy SimCard
# 5) Dodaj ponizsze kontakty:
#    - "Ola", 98765432
#    - "Adam", 12345678
#    - 100, 12345678
#    - "Kasia", "numer"
#   Czesc danych jest nieprawidiowa, wiec nie powinny byc dodane przez addContact
# 6) Wyswietl kontakty z showContacts()

class SimCard:
    def __init__(self) -> None:
        self.contacts = []
    
    def addContact(self, name, telephone):
        if isinstance(name, str) == False: return
        if isinstance(telephone, int) == False: return

        user = {
            "name": name,
            "telephone": telephone
        }
        self.contacts.append(user)
    
    def showContacts(self):
        for i in self.contacts:
            print(i["name"] + " " + str(i["telephone"]))

sim = SimCard()
sim.addContact("Ola", 98765432)
sim.addContact("Adam", 12345678)
sim.addContact(100, 12345678)
sim.addContact("Kasia", "numer")

sim.showContacts()