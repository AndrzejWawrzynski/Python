import os
import pickle

scriptData = os.path.dirname(__file__)

class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
    
    def __str__(self):
        return str(self.name) + " " + str(self.surname) + " " + str(self.city)
    
person1 = Person("Ola", "Kowalska", "Krk")
person2 = Person("Adam", "Twardowski", "Waw")
person3 = Person("Kasia", "Dluga", "Gda")

people = [person1, person2, person3]

fh = open(scriptData + "/people.dat", "wb")
# pickle.dump(person1, fh)
# pickle.dump(person2, fh)
# pickle.dump(person3, fh)
pickle.dump(people, fh)
fh.close()


fh = open(scriptData + "/people.dat", "rb")
listFromFile = pickle.load(fh)
fh.close()

print(listFromFile)

for i in listFromFile:
    print(i)