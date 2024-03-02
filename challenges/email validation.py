# String i find()
# 1) Napisz funkcje validateEmail sprawdzajaca w podstawowy
#    sposob czy email jest prawidlowy.
# 2) Wykorzystaj find() do wyszukania fragmentow tekstu w email:
#   - sprawdz czy istnieje w przekazanym do funkcji emailu
#   znak @, zapisz index w monkeyIndex
#   - posiadajac pozycje @ sprawdz czy istnieje znak
#   kropki po malpie. Zapisz pozycje kropki w dotIndex
#   - jezeli wszystkie powyzsze warunki sa spelnione
#   zwroc True, w innym wypadku False
# 3) Wywotaj funkcje z nastepujacymi mailami, pokaz
#    w konsoli co zwraca funkcja:
#    - asia@example.com
#    - karol@domena
#    - user.com

def validateEmail(email):
    monkeyIndex = email.find("@")
    if monkeyIndex < 0: return False

    dotIndex = email.find(".")
    if dotIndex == -1: return False
    if dotIndex < monkeyIndex: return False

    return True

def validateEmail2(email):
    monkeyIndex = email.find("@")
    if monkeyIndex < 0: return False

    dotIndex = email.rfind(".")
    lenEmail = len(email)
    if dotIndex == -1: return False
    if dotIndex == lenEmail - 1: return False
    if dotIndex < monkeyIndex: return False

    return True

email1 = "asia@exaple.com"
print(email1, validateEmail(email1))

email2 = "karol@domena"
print(email2, validateEmail(email2))

email3 = "user.com"
print(email3, validateEmail(email3))

email4 = "asia.kowalska@user.com"
print(email4, validateEmail2(email4))

email5 = "asia.kowalska@user."
print(email5, validateEmail2(email5))

email6 = ".kowalska@user.com"
print(email6, validateEmail2(email6))