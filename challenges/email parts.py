# String - zadanie:
# 1) Napisz funkcje getEmailParts przyjmujaca
#    parametr email.
# 2) Wykorzystaj pobieranie fragmentow tekstu w python aby rozlozyc
#    email na czesci i zapisz je w zmiennych:
#    - user - od poczatku emaila do ostatniego znaku przed @
#    - domainName - tekst za @ i przed kropka
#    - domainExt - tekst za ostatnia kropka do konca
# Uwaga: pamietaj ze okreslajac poczatek i koniec fragmentu z stringa
# mozesz korzystaé z zmiennych np:
# monkey Ind = 5
# user = email [@:monkeyInd]
# 3) Zwroc slownik z funkcji z elementami jak powyzsze
#    zmienne. Pamietaj aby uzyc find aby okreslic
#    pozycie indeksu malpy w email, jesli go nie ma
#    zwroc None z funkcji, podobnie z kropka.
# 4) Pretestuj funkcje na emailu:
#    ola@domena.com
#    W konsoli powinna pojawic sie informacja:
#    {'user': 'ola', 'domainName': 'domena', 'domainExt': 'com' }

def getEmailParts(email):
    monkeyIndex = email.find("@")
    if monkeyIndex <= 0: return None
    user = email[:monkeyIndex]
    # print(user)
    if email[0] == ".":return False
    dotIndex = email.rfind(".")
    lenEmail = len(email)
    if dotIndex <= 0: return None
    if dotIndex == lenEmail - 1: return False
    if dotIndex < monkeyIndex: return False
    domainName = email[monkeyIndex+1:dotIndex]
    # print(domainName)
    domainExt = email[dotIndex+1:]
    # print(domainExt)
    emailParts = {"user": user, "domainName" : domainName, "domainExt" : domainExt}
    return emailParts



print(getEmailParts("ola@domena.com"))
