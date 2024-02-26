# Stworz funkcje do konwersji czasu:
# 1) convertToSeconds przyjmujaca ilos godzin
#    oraz minut i zwracajaca ilosc sekund.
#    Jako parametry funkcji zapisz: hours, minutes.
#    Skonwertuj 3 godziny i 25 minut na sekundy,
#    wynik pokaz w konsoli.
# 2) convertToHours przyjmujaca parametr minutes
#    oraz zwracajac ilos godzin.
#    Skonwertuj 120 minut na godziny i pokaz
#    wynik w konsoli.

def convertToSeconds(hours,minutes):
    return (hours * 60 * 60) + minutes * 60

seconds = convertToSeconds (3, 25)
print("Ilosé sekund:", seconds)

def convertToHours(minutes):
    return minutes / 60

hours = convertToHours (120)
print("Ilosé godzin:", hours)