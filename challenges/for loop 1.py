# Liczby nieparzyste dodane do set
# 1) Dodaj liste numbers z wartosciami od -3 do 3 z krokiem co 1
# 2) Dodaj set z wartoscia poczatkowa -1
# 3) Stwórz petle for in z tablica numbers
# 4) W kazdej iteracji petli sprawd czy liczba z listy jest nieparzysta,
#    czyli reszta z dzielenia przez dwa nie moze byé równa zero (!= 0).
#    Dodaj nieparzysta liczbe do zestawu.
# 5) Wyswietl w konsoli nieparzyste liczby w set z pomoca petli for

numbers = [-3,-2,-1,0,1,2,3]
setData = {-1}
for i in numbers:
    if i % 2 != 0:
        setData.add(i)

for i in setData:
    print(i)