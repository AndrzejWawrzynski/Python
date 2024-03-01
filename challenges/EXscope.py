# Pracownicy w liscie z zwiekszona pensja
# 1) Stworz globalna zmienna employees, któa jest pusta lista
# 2) Napisz funkcje addEmployee która przyjmuje email i salary, wewnatrz stworz
#    slownik z tymi samymi parametrami. Nastepnie dodaj go do globalnej listy
#    employees stosujac funkcje append np someList. append (newElement)
# 3) Wywolaj funkcje addEmployee dla trzech dowolnych pracownikow
#    o pensjach: 6000, 8000 i 10000, wpisz dowolne maile
# 4) Dodaj funkcje increaseSalary z dwoma argumentami: employees i pctIncrease
#    Jako pierwszy argument bedzie przekazywana lista pracownikow, a do drugiego
#    wartos podwyzki np. 15 Przejdz po wszystkich pracownikach i zwieksz
#    pensje pracownikow o przekazana wartosc procentowa petIncrease
# 5) Zwieksz pensje pracowników z funkcja increaseSalary o 20%, wyswietl
#    liste w terminalu

employees = []

def addEmployee(email, salary):
    user = {
        "email" : email,
        "salary" : salary
    }
    employees.append(user)

addEmployee("aaa@mail.eu", 6000)
addEmployee("bbb@mail.eu", 8000)
addEmployee("ccc@mail.eu", 10000)

print(employees)

def increaseSalary(employees, pctIncrease):
    pctIncrease *= 0.01
    for i in employees:
       i["salary"] *= 1 + pctIncrease

a = 20
increaseSalary(employees, a)

print(employees)