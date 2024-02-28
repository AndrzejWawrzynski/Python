# Zadanie na przekazanie danych funkcji przez wartosc
# 1) Napisz funkcje increaseSalary z dwoma parametrami
#    liczbowymi: money oraz bonus
# 2) W funkcji podnies wartosc money o 20%.
#    Nastepnie zwroc sume money i bonus.
# 3) Stworz zmienna salary poza funkcja o wartosci 5000
# 4) Wywolaj funkcje increaseSalary przekazujac jako
#    argument salary oraz 1000 jako bonus. Zachowaj
#    zwracana wartosc w zmiennej newSalary.
# 4) Pokaz w konsoli wartosci: salary i newsalary,
#    poniewaz przekazywane dane sa niemutowalne to salary
#    musi miec wartose 5k, a newsalary odpowiednio wieksza
#    wedlug implementacji funkcji.

def increaseSalary(money, bonus):
    money = money * 1.2
    return money + bonus

salary = 5000
newSalary = increaseSalary(salary, 1000)
print("Salary = ", salary)
print("nweSalary = ", newSalary)
