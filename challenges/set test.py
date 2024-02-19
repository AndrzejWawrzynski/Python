# 1. Stworz set z unikalnymi wartosciami jak:
#    Ania, Kasia, Ola, Karol, Daniel, Zuza
# 2. Dodaj do set za pomoca funkcji add kolejne elementy:
#    Olek, Basia, Kasia, Karol, Zuza, Paulina
# 3. Pokaz w konsoli wielkosc set
# 4. Wykorzystaj petle for aby pokazaé elementy w set

setData = {"Ania", "Kasia", "Ola", "Karol", "Daniel", "Zuza"}

setData.add("Olek")
setData.add("Basia")
setData.add("Kasia")
setData.add("Karol")
setData.add("Zuza")
setData.add("Paulina")

print("Ilosc elementow w setdata: ", len(setData))

for i in setData:
    print(i)