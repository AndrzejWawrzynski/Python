# opratory tozsamosci

strData = "test"

print(dir(strData))

print(strData.upper())

intdata = 10
print(dir(intdata))

a = [1,2,3,4,5]
b = a

print(a is b)
a.append(77)
print(a)
print(b)

print(a is not b)

c = [3,4,5]

print(a is c)

print(a is not c)


