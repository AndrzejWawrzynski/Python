# 1. Stworz krotke z ostantnimi wydatkami na koncie
#    bankowym z wartosciami: 100, 200, 300, 400, 500, 600
# 2. Policz wydatki z pomoca petli for i wyswietl w konsoli
#    ostateczna kwote. Pamietaj aby stworzyé zmienna
#    z wartoscia poczatkowa 0 do której dodasz kolejny wydatek

expenses = (100, 200, 300, 400, 500, 600)
sum = 0
for i in expenses:
    sum = sum + i

print("Suma wydatkow to:", sum)