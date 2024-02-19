
setData = {2,3,1,4,5}
setData.add(22)

setData.discard(1)

print(type(setData))
print(setData)

for i in setData:
    print(i)

frozenData = frozenset(setData)

print(type(frozenData))

# frozenData.add(1) # AttributeError: 'frozenset' object has no attribute 'add'

for i in frozenData:
    print(i)
