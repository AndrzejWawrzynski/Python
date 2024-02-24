# Napisz program decydujacy czy wyjsc czy zostac w domu zaleznie od pogody
# 1) Dodaj zmienne:
#    - raining = False
#    - haveUmbrella = False
#    - temperature = 14
# 2) Sprawdé czy temperatura jest powyzej lub równa 40 lub ponizej lub równa 0
#    w takim wypadku wyswietl "Zostan w domu"
# 3) Jezeli powyzszy warunek nie jest spelniony w elif sprawdz kolejny czy
#    temperatura jest powyzej 0 oraz ponizej 10 stopni oraz ma parasolke
#    i pada, w takim wypadku wyswietl: "Mozesz wyjsé z parasolka"
# 4) Gdy zadne z powyzszych nie jest spelnione sprawdz w kolejnym elif
#    czy nie pada i temperatura jest powyzej lub rowne 10 to wyswietl:
#    "Mozesz wyjsc bez parasolki"
# 5) Na koniec dodaj ostatnia domyslna opcje z informacja "Zostan w domu"

raining = False
haveUmbrella = False
temperature = 14

if temperature >= 40 or temperature <= 0:
    print("Zostan w domu")
elif temperature > 0 and temperature < 10 and haveUmbrella and raining:
    print("Mozesz wyjsc z parasolka")
elif temperature >= 10 and not raining:
    print("Mozesz wyjsc z domu")
else:
    print("Zostan w domu")