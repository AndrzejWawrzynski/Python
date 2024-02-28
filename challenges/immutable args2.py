# Zadanie: Obliczanie ostatecznej ceny produktu po rabacie
#
# Cel: Napisz program, ktory oblicza ostateczna cene produktu po zastosowaniu rabatu.
# Program powinien prosic uzytkownika o wprowadzenie ceny poczatkowej produktu
# oraz wielkosci rabatu w procentach, a nastepnie obliczyc i wyswietlic cene koncowa.
# Kroki do wykonania:
# 1) Napisz funkcje calculateFinalPrice, która przyjmuje dwa parametry:
#    initialPrice (cena poczatkowa produktu) oraz discount (rabat w procentach).
# 2) W funkcji oblicz cene produktu po rabacie i zwroc te wartosc.
# 3) Popros uzytkownika o prowadzenie ceny poczatkowej produktu oraz wielkosci rabatu.
# 4) Wywolaj funkcje calculateFinalPrice z wprowadzonymi wartosciami i przechowaj wynik.
# 5) Wyswietl ostateczna cene produktu.

def calculateFinalPrice(initialPrice, discount):
    discount = discount/100
    return initialPrice - (initialPrice * discount)

initialPrice = float(input("Podaj cene produktu : "))
discount = float(input("Podaj wielkosc rabatu :"))

priceAfterDiscount = calculateFinalPrice(initialPrice, discount)
print("Cena produktu z rabatem ", int(discount), "% to : ", priceAfterDiscount)