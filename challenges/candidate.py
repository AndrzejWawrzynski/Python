# Napisz program sprawdzajacy wymagania potencjalnego kandydata na programiste
# 1) Dodaj zmienna experience z wartoscia 2, kolejna languages z lista elementów:
#    "python", "typescript", "javascript", "java"
#    Ostatnia zmienna bedzie contractType o wartosci "b2b" jaka chce kandydat
# 2) Wykorzystaj instrukcje if z operatorem and do sprawdzenia czy
#    doswiadczenie kandydata to dwa lub wiecej lat oraz czy zna jezyk python
#    i java. Pamietaj o wykorzystaniu operatora in do sprawdzenia czy
#    wartosé jest w liscie
# 3) Jesli powyzsze warunki sa spelnione zrób kolejny if i sprawdz czy
#    typ kontraktu jest "b2b" lub "employment", pamietaj o uzyciu operatora or.
#    Zaprezentuj w terminalu informacje ze kandydat jest przyjety, gdy warunki
#    sa speinione.
# 4) W przypadku, gdy warunki w if nie sa speinione pokaz w konsoli po else
#    odpowiednia informacje

experience = 2
languages = ["python", "typescript", "javascript", "java"]
contractType = "b2b"

if experience >= 2 and "python" in languages and "java" in languages:
    if contractType == "b2b" or contractType == "employment":
        print("Pracownik spelnia warunki do zatrudnienia")
    else:
        print("Pracownik nie spelnia wymogu typu zatrudnienia:", contractType)
else:
    print("Kandydat nie spetnia podstawowych warunkow")
    