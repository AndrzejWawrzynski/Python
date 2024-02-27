# Napisz dwie funkcje konwertujace temperature:
# 1) Funkcja cToF skonwertuje stopnie Celsjusza na Fahrenheita z wzoru:
#    fahrenheit = celsius * 9 / 5 + 32
# 2) Funkcja fToC konwertuje stopnie Fahrenheita na Celsjusza z wzoru:
#    celsius = （fahrenheit - 32） * 5 / 9；
# 3) Dodatkowo w konsoli pokaz wynik konwersji np:
#    "20 stopni Celsjusza to 68 stopni Fahrenheita" itd.
#    Jesli chcesz uzyj w string specjalnego znaku stopni ° za pomoca \xBO
# 4) Skonwertuj 20°C na Fahrenheita (68°F)
#    Skonwertuj 86°F na Celsjusza (30°C)

def cToF(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return int(fahrenheit)

def fToC(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return int(celsius)

tempC = 20
print(str(tempC)+"\xB0 Celsjusza to " + str(cToF(tempC)) + "\xB0 Fahrenheita")

tempF = 86
print(str(tempF)+" stopni Fahrenheita to " + str(fToC(tempF)) + " stopni Celsjusza")


def cToF2(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "stopni Celsjusza to", fahrenheit, "stopni fahrenheita")
    return fahrenheit

def fToC2(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit, "\xB0 fahrenheita to", celsius, "\xB0 celsjusza")
    return celsius

f = cToF2(20)
c = fToC2(86)