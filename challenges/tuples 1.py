# 1. Stwórz krotke z wartosciami: 50, 100, 150, 200, 250
# 2. Pokaz typ krotki w konsoli
# 3. Pokaz w konsoli ilosc elementow krotki
# 4. Pokaz ostatni element krotki wykorzystujac len() -1
# 5. Nastepnie pokaz lementy od drugiego do czwartego
# 6. Pokaz trzeci element od konca z ujemnym indeksem

numbers = (50, 100, 150, 200, 250)
print(type(numbers))
print(len(numbers))
print("Ostatni element:", numbers[ len(numbers)-1 ])
print("Ostatni element:", numbers[-1])
print(numbers[1:])
print(numbers[1:5])
print(numbers[-3])