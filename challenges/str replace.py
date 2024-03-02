#
# Zadanie String replace
# 1) Stworz funkcje cleanText, ktora bedzie czyscic
#    przekazany tekst z okreslonych slow.
# 2) Uzyj funkcje replace do zamiany podanych slow na
#    wykropkowane, ktore wielokrotnie moze pojawic sie
#    w przekazanym lancuchu. Dla uproszczenia bedziesz
#    zamieniac nazwy jezykow programowania ;) np.
#    php zmienisz na ***, java na **** itd
# 3) Zastap nastepujace slowa kluczowe:
#    JavaScript, java, php, html, css
# 4) Zwroc wyczyszczony tekst z funkcji cleanText.
# 5) Wywolaj funkcje na nastepujacym lub podobnym tekscie:
#    """Programowanie zaczalem z jezykiem php, nastepnie
#    poznalem: html i css, ale obecnie skupiam sie na
#    JavaScript"""
# Wynik pokaz w konsoli.

def cleanText(text):
    text = text.replace("JavaScript", "**********")
    text = text.replace("java", "****")
    text = text.replace("html", "****")
    text = text.replace("php", "***")
    text = text.replace("css", "***")
    return text

text = """Programowanie zaczalem z jezykiem php, nastepnie 
poznalem: html i css, ale obecnie skupiam sie na 
JavaScript"""

newText = cleanText(text)
print(newText)