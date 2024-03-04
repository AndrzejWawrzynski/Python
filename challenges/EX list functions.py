# Zadanie - organizacja imprezy
# W tym zadaniu skorzystasz z operacji na listach do zorganizowania listy gosci
# oraz listy potraw na imprezie. Nauczysz sie dodawac, usuwac elementy,
# sortowac listy oraz wykonywac inne podstawowe operacje.
#
# 1) Stworz liste 'guests' z piecioma imionami gosci.
# 2) Wyswietl dlugosc listy gosci, aby sprawdzic, ilu masz gosci.
# 3) Dodaj jeszcze dwoch gosci na koniec listy.
# 4) Jeden z gosci nie moze przyjsc. Usun go z listy.
# 5) Posortuj liste gosci alfabetycznie i wyswietl ja.
# 6) Stwórz liste 'dishes' z trzema potrawami.
# 7) Dodaj do listy potraw jeszcze dwie nowe potrawy.
# 8) Wyswietl potrawe, która znajduje sie na srodku listy.
# 9) Usun ostatnia potrawe z listy.
# 10) Sprawdz, czy na liscie potraw znajduje sie 'Pizza'. Jesli tak,
#     wyswietl komunikat "Pizza jest na liscie!", w przeciwnym razie
#     dodaj Pizze do listy potraw.
#

guests = ["Adam", "Robert", "Kasia", "Ola", "Ela"]
print(len(guests))
guests.append("Leo")
guests.append("Zuzia")
guests.remove("Robert")
guests.sort()
print(guests)

dishes = ["Zupa", "Bigos", "Ciasto"]
dishes.extend(["Tort","Salatka"])
print(dishes)

midDishes = len(dishes) // 2
print(dishes[midDishes])

dishes.pop()
print(dishes)

if "Pizza" in dishes:
    print("Pizza jest na liscie")
else:
    dishes.append("Pizza")
    print("Dodano pizze do listy")
print(dishes)