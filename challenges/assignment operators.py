# Zadanie - operacje na rachunku bankowym, skorzystaj
# z skroconych operatorow przypisania z operacja
# matematyczna np: += -= *= /= itd
# Uwaga, po kazdej operacji wyswietl saldo w konsoli
# 1) Stworz zmienna balance z wartoscia poczatkowa 1000
# 2) Dodaj wartosc nowej pensji 7000
# 3) Odejmij 2000 kosztow za mieszkanie
# 4) Blad banku pomnozyl Twoje saldo trzykrotnie
# 5) Odejmij 4000 na komputer
# 6) Bank zorientowal sie ze powstal blad i cofa ostatnie
#    transakcje. Dodaj do salda 4000, podziel je przez 3
#    i dopiero teraz odejmij 4000
# 7) Pokaz saldo koncowe

balance = 1000; print(balance)
balance += 7000; print(balance)
balance -= 2000; print(balance)
balance *= 3; print(balance)
balance -= 4000; print(balance)
balance += 4000; print(balance)
balance /= 3; print(balance)
balance -= 4000; print(balance)
print("Saldo koncowe:", balance)

print("-----------------")

balance = 1000
balance += 7000
print("saldo po wplywie pensji: " + str(balance) )
balance -= 2000
print("saldo po wydatkach na mieszkanie: ", balance)
balance *= 3
print("saldo po biedzie banku: ", balance)
balance -= 4000
print("saldo po zakupie komputera: ", balance)
balance = ( (balance + 4000) / 3) - 4000
print("saldo po poprawieniu bledu banku: ", balance)