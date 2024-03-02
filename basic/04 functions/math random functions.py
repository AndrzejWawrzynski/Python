import random
import math

print(type(str(12))) # <class 'str'>
print(type(str([1,2,3,4]))) # <class 'str'>

number = int("123")
print(type(number)) # <class 'int'>

number += 10
print(number) # 133

floatNum = float("45.67")
print(type(floatNum)) # <class 'float'>
floatNum = floatNum * 2
print(floatNum) # 91.34

print(abs(9)) # 9
print(abs(-9.1)) # 9.1

print(math.ceil(11.0001)) # 12
print(math.ceil(9.999999)) # 10
print(math.ceil(-1.00001)) # -1
print(math.ceil(-1.9999999)) # -1

print(math.floor(11.001)) # 11
print(math.floor(11.9999)) # 11
print(math.floor(5.12)) # 5
print(math.floor(-5.12)) # 6
print(math.floor(-5.99)) # 6

print(max(10,1,-9,33,89,0)) # 89
print(max([10,1,-9,33,89,0])) # 89
print(max((10,1,-9,33,89,0))) # 89

print(min(1,4,-9,45,-3,5,-12)) # -12
print(min([1,4,-9,45,-3,5,-12])) # -12
print(min((1,4,-9,45,-3,5,-12))) # -12

print( 4 ** 3) # 64
print(pow(4,3)) # 64

print(math.sqrt(128)) # 11.313708498984761

print(round(12.78912345, 5)) # 12.78912
print(round(12.78912345, 4)) # 12.7891
print(round(12.78912345, 3)) # 12.789
print(round(12.78912345, 2)) # 12.79
print(round(12.78912345, 1)) # 12.8

print(random.random())

print(random.choice([0,1,2,3,4,5,6,7]))
print(random.choice(("Ania","Ola","Kasia")))

print(random.randrange(1,11))


print(round(random.uniform(1,10),2))




