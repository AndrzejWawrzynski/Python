# Zadanie: Wyswietlanie listy zakupow
#
# Cel: Napisz program, który tworzy i wyswietla liste zakupow na podstawie
#      wrowadzonych przez uzytkownika produktow.
#      Program nie bedzie zwracal zadnej wartosci, ale bezposrednio wyswietli liste zakupow w konsoli.
# Kroki do wykonania:
# 1) Zdefiniuj funkcje displayShoppingList, która przyjmuje jeden parametr: shoppingList.
#    Funkcja ta powinna wyswietlac wszystkie elementy listy zakupow, kazdy element w nowej linii.
# 2) Stwórz pusta liste zakupow.
# 3) W petli, popros uzytkownika o wprowadzenie nazwy produktow do listy zakupów,
#    az do wpisania stowa "koniec".
# 4) Po zakonczeniu wprowadzania, wywotaj funkcie displayShoppingList, przekazujac jej liste zakupow.

def displayShoppingList(shoppingList):
    print("Twoja lista zakupow :")
    for i in shoppingList:
        print(" - ", i)

shoppingList = []

while True:
    product = input("Wprowac nazwe produktu do listy lub 'koniec' aby zakonczyc : ")
    if product == "koniec":
        break
    shoppingList.append(product)

displayShoppingList(shoppingList)

