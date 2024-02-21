# 1) Oblicz zwrot z inwestycji po roku, zapisz ponizsze
# zmienne:
#  - capital - 5000
#  - rateOfInterest - 0.08 czyli 8%
#  - inflationRate - 0.15 czyli 15%
# 2) Oblicz zwrot z inwestycji oraz o ile spadla wartosc
#    kapitatu z uwagi na inflacje, pokaz te kwoty w konsoli
# 3) Dodaj do kapitalu zwrot z inwestycji oraz odejmij
#    utracony kapitat z uwagi na inflacje, pokaz wartosc
#    koncowa w konsoli

capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

earnedMoney = capital * rateOfInterest
print ("Zarobiona kwota:", earnedMoney)

lostMoney = capital * inflationRate
print("Utracona kwota:", lostMoney)

newCapital = capital + earnedMoney - lostMoney
print("Kwota koncowa:", newCapital)
