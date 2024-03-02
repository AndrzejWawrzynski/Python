# Zadanie - symulacja kosztów podrozy

# W tym zadaniu skorzystasz z funkcji matematycznych i losowych
# do symulacji kosztow podrozy. Uzyj danych typow, funkcji matematycznych
# oraz funkcji z modulu random do wyliczenia i przewidzenia kosztow.
# 1) Stwórz zmienna 'distance z losowa wartoscia od 100 do 1000, która
#    oznacza dystans w kilometrach do pokonania.
# 2) Oblicz spodziewane spalanie na podroz, przyjmujac ze na 100 km
#    spala sie 7 litrow paliwa. Uzyj zaokraglenia w gore.
# 3) Przyjmij cene paliwa za litr jako losowa wartosc zmiennoprzecinkowa
#    miedzy 4.5 a 5.5. Zaokraglij cene do dwoch miejsc po przecinku.
# 4) Oblicz calkowity koszt paliwa na podroz.
# 5) Jesli koszt paliwa przekracza 400 z1, wyswietl komunikat o wysokich
#    kosztach podrozy. W przeciwnym razie, poinformuj o przystepnych kosztach.
#
import math
import random

distance = random.randrange(100,1000)
print("Dystans w km :", distance)

fuelConsumption = math.ceil(distance/100*7)
print("Spodziewane spalanie paliwa na cala podroz :", fuelConsumption)

fuelCost = round((random.uniform(4.5,5.5)) * fuelConsumption, 2)
print("Koszt paliwa to :",fuelCost)

if fuelCost > 400:
    print("Wysokie koszty podrozy")
else:
    print("Przystepne koszty podrozy")