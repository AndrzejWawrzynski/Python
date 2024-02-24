
number = 5

while number > 0:
    print(number)
    number -= 1

number = 1

while number < 6:
    print(number)
    number += 1

num = 0

while True:
    print("Wprowac liczbe lub exit aby zakonczyc")
    strData = input()
    if strData == "exit": break
    num += int(strData)
    print("Wartos po dodaniu liczby :" + str(num))

print("Wartosc koncowa :" + str(num))

number = 3

while number > 0:
    print(number)
    number -= 1
else:
    print("Wartosc number po petli : " + str(number))