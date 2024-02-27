# Zadanie: Kalkulator wieku psa w ludzkich latach
#
# Cel: Napisz program, który przelicza wiek psa na ludzkie lata. Program powinien prosic uzytkownika
# o wrowadzenie wieku psa, a nastepnie obliczyé i wyswietlic jego wiek w ludzkich latach.
# Pierwsze dwa lata zycia psa liczymy jako 10.5 ludzkiego roku za kazdy, a kazdy kolejny
# rok jako 4 ludzkie lata.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcje calculateHumanYears, która przyjmuje wiek psa jako parametr.
#    W funkcji uzyj instrukcji if-elif-else do obliczenia wieku psa w ludzkich latach.
#    Dla uproszczenia zalozmy ze ilos lat miejsza rowna 2 musi by pomnozona przez 10.5,
#    a dla wiekszych wartosci od 2 trzeba zastosowaé dziatanie 21 + (dogYears - 2) * 4
# 2) Uzyi petli, aby umozliwic uzytkownikowi wielokrotne uzywanie kalkulatora bez
#    restartowania programu.
# 3) Popros uzytkownika o wprowadzenie wieku psa.
# 4) Wywotaj funkcje calculateHumanYears i przekaz jej wiek psa prowadzony przez uzytkownika.
# 5) Wyswietl obliczony wiek psa w ludzkich latach.
#

def calculateHumanYears(dogYears):
    if float(dogYears) <= 2 and float(dogYears) > 0:
        humanYears = float(dogYears) * 10.5
        print("Wiek pas to : ", dogYears)
        print("Wiek psa na ludzkie lata to :", humanYears)
    elif float(dogYears) > 2:
        humanYears = 21 + (float(dogYears) - 2) * 4
        print("Wiek pas to : ", dogYears)
        print("Wiek psa na ludzkie lata to :", humanYears)
    else:
        print("Wprowadz poprawny wiek")


while True:   
    dogYears = input("Wprowadz wiek psa lub 'exit' aby zakonczyc :")
    if str(dogYears) == "exit":
        break
    calculateHumanYears(dogYears)

