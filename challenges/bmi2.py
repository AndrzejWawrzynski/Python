# Zadanie: Kalkulator BMI z funkcja
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcje calculateBMI, ktora przyjmuje wage w kilogramach i wrost w centymetrach.
#    Funkcja powinna obliczac BMI i zwracac wartose BMI wedlug wzoru:
#    weight / ( (height / 100) ** 2)
# 2) Zdefiniuj funkcje classifyBMI, ktora przyjmuje wartosé BMI i klasyfikuje ja
#    do odpowiedniego przedzialu.
#    bmi < 18.5 z info: Masz niedowage.
#    bmi < 25 z info: Twoja waga jest w normie.
#    bmi < 30 z info: Masz nadwage.
#    reszta wartosci to: "Masz spora nadwage."
# 3) Popros uzytkownika o wrowadzenie wagi i wzrostu.
# 4) Wywolaj funkcje calculateBMI, aby obliczy BMI na podstawie danych uzytkownika.
# 5) Wywolaj funkcie classifyBMI, aby okreslié przedziat BMI i wyswietlic odpowiedni komunikat.
#

def calculateBMI(weight, height):
    return weight / ( (height / 100) ** 2)

def classifyBMI(BMI):
    if BMI < 18.5:
        print("Masz niedowage.")
    elif BMI < 25:
        print("Twoja waga jest w normie.")
    elif BMI < 30:
        print("Masz nadwage.")
    else:
        print("Masz spora nadwage.")

while True:
    weight = float(input("Podaj swoja wage w kg :"))
    height = float(input("Podaj swoj wzrost w cm :"))
    BMI = calculateBMI(weight, height)
    print("Twoje BMI to :", float(round(BMI,2)))
    classifyBMI(BMI)

    again = input("Czy chcesz obliczy ponownie BMI? (tak/nie):")
    if again.lower() != "tak":
        break

