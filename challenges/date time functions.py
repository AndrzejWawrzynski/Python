# Zadanie - sledzenie czasu pracy nad projektem
# W tym zadaniu uzyjesz modulow time i datetime do symulacji prostego
# systemu sledzenia czasu pracy nad projektem. Nauczysz sie uzywac
# roznych funkcji zwiazanych z czasem i data.
#
# 1) Uzyj modulu datetime, aby zapisac czas rozpoczecia pracy nad projektem
#    jako zmienna 'start_time'.
# 2) Symuluj prace nad projektem przez wywotanie time.sleep() z losowo
#    wybranym krotkim czasem (np. od 1 do 5 sekund) 
# 3) Uzyj modulu datetime ponownie, aby zapisac czas zakonczenia pracy
#    nad projektem jako zmienna 'end_time'.
# 4) Oblicz laczny czas pracy nad projektem przez odjecie 'start_time"
#    od 'end_time' i wyswietl wynik.
# 5) Jesli laczny czas pracy przekracza 3 sekundy, wyswietl komunikat
#    o duzej ilosci wlozonego czasu, w przeciwnym razie poinformuj o krotkim czasie pracy.

import datetime
import time
import random

start_time = time.perf_counter()

t = round(random.uniform(1,5), 5)
time.sleep(t)
print("random = ", t)

end_time = time.perf_counter()

time_work = round(end_time - start_time, 5)

x = False
if time_work > 3:
    print("Duza ilosc wlozonego czasu")
    x = True
    print("time_work :", time_work, "seconds")
if not x:
    print("Krotki czas pracy")
    print("time_work :", time_work, "seconds")