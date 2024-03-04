
data = {"name":"Ola", "city":"Waw"}
print(data["name"])

dataPostalCode = "postaCode"
data[dataPostalCode] = 12345
data["street"] = "Green"
print(data)

print(len(data))

del data["city"]
print(data)
data.clear()
print(data)

data = {"name":"Kasia", "city":"Krk"}
dataCopy = data.copy()
print(dataCopy)
print(data["name"] is dataCopy["name"])

print(data is dataCopy)

data2 = dict.fromkeys(("name", "cit", "code"))
print(data2)

data3 = dict.fromkeys(("name", "cit", "code"), 0)
print(data3)

print(data2.get("x", "DEFAULT"))

print("name" in data2)

print(data2.keys())
print(data2.values())