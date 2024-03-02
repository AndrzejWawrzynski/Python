# Zadanie z lambda i map
# 1) Stworz liste names z wartosciami: Ola, Ania, Kasia
# 2) z pomoca mapy i lambdy dodaj do kazdego imienia tekst " Kowalska"
# 3) Wyswietl nowa liste w konsoli
# 4) Prefiltruj nowa liste ze wzgledu na dlugosc tekstu, zachowaj
#    w nowej liscie tylko te ktore maja wiecej niz 12 znakow
#    Pokaz prefiltrowana liste w konsoli

names = ["Ola", "Ania", "Kasia"]

result = list(map(lambda a: a + " Kowalska", names))
print(result)

result2 = list(filter(lambda a: len(a) > 12, result))
print(result2)