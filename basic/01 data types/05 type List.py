
list = ["Ola", "Ania", 23, 99, "Rafal"]
print(type(list))
print(list)

print(list[0])
print(len(list))
print(list[4])
print(list[len(list)-1])
# print(list[5]) IndexError: list index out of range

print(list[-1])
print(list[-2])
# print(list[-6]) IndexError: list index out of range

print(list[1:4]) # ['Ania', 23, 99]
print(list[2:]) # [23, 99, 'Rafal']

list[0] = "Kasia"
print(list)

del list[2]
print(list)

print(99 in list) # True
print("Rafal" in list) # True
print("Ola" in list) # False

if "Ania2" in list:
    print("Ania jest w liscie")
    print("Kolejny kod")

print("Dalszy kod")

for i in list:
    print(i)

data = [["Daniel","Rafal"],
         ["Kasia", "Ania"],
         ["Ola","Adam"]
         ]

print(len(data))

print(data[1][0])
print(data[2][1])

data1 = [1,2,3]
data2 = [4,5,6]

numbers = data1 + data2
print(numbers)

numbersX2 = numbers * 2
print(numbersX2)
