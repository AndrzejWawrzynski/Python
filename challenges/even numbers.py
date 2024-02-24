# 1) Stwórz krotke z wartosciami od 1 do 10
# 2) Zrob petle for in z krotka i wyswietl w konsoli
#    tylko parzyste liczby. Skorzytaj z instrukcji
#    warunkowej if oraz operatora % zwracajacego reszte
#    z dzielenia. Jesli reszta z dzielenia przez 2
#    bedzie równa 0 to nie ma reszty, tym samym liczba
#    jest parzysta

numbers = (1,2,3,4,5,6,7,8,9,10)

for i in numbers:
    if i % 2 == 0:
        print(i)