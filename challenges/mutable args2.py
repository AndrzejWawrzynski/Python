# Cel: Napisz program, ktory analizuje prowadzone temperatury i wykrywa ich srednia,
# najnizsza oraz najwyzsza wartosc. Program powinien prosic uzytkownika o wprowadzanie
# temperatur jedna po drugiej, a nastepnie zwracac raport analizy.
# Komentarze w kodzie beda po polsku, a nazwy zmiennych i funkcji po angielsku.
#
# Kroki do wykonania:
# 1) Popros uzytkownika o prowadzenie serii temperatur, gdzie kazda temperatura wrowadzana jest
#    oddzielnie, a zakonczenie prowadzania sygnalizowane jest przez wpisanie 'koniec'.
# 2) Dla kazdej wrowadzonej temperatury, dodaj ja do listy temperatur po konwersji na typ float.
# 3) Po zakonczeniu wrowadzania danych, wywolaj funkcje analizujaca temperatury, ktora zwraca
#    krotke zawierajaca srednia, maksymalna i minimalna temperature z listy.
#    Uwaga aby pobrac wartosc minimalna z listy wykorzystaj funkcje min() do ktorej przekazesz
#    liste wartosci liczbowych, tak samo max() oraz sum()
# 4) Wyswietl wyniki analizy uzytkownikowi.
#
# Rozwiazanie:


def analizeTemperatures(temperatures):
    avgTemp = round(sum(temperatures) / len(temperatures),2)
    minTemp = round(min(temperatures),2)
    maxTemp = round(max(temperatures),2)

    return (avgTemp, minTemp, maxTemp)

temperatures = []
while True:
    temp = input("Podaj temperature w stopniach Celcjusza lub 'koniec' aby zakonczyc :")
    if temp.lower() == "koniec":
        break

    temperatures.append(float(temp))

data = analizeTemperatures(temperatures)
avg = data[0]
min = data[1]
max = data[2]

print("Srednia temperatura to : " + str(avg) + "\xB0 C")
print("Minimalna temperatura to : " + str(min) + "\xB0 C")
print("Malsymalna temperatura to : " + str(max) + "\xB0 C")


avgTemp, minTemp, maxTemp = data
print ("avgTemp:", avgTemp)
print ("minTemp:", minTemp)
print ("maxTemp:", maxTemp)
