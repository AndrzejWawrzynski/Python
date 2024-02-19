
contacts = {
    "Ola" : "ola@exaple.com",
    "Daniel" : 30,
    "Ania" : "ania@exaple.com"
}

contacts["Rafal"] = "rafal@exaple.com"

print(contacts["Ola"])
print(contacts["Daniel"])

print(type(contacts))

print(len(contacts))

print(contacts.keys())
print(contacts.values())

for i in contacts:
    print(i + " " + str(contacts[i]))


for i, n in contacts.items():
    print( i, n)