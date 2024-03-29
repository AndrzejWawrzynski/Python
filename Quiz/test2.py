i = [2**n for n in range(11)]

for a in i:
    print(a)

import random

mylist = ["apple", "banana", "cherry"]

l=random.choices(mylist, weights = [8, 1, 1], k = 10)
print(l)
print(l.count("apple"))