
class Vehicle:
    def __init__(self, brand, name):
        self.brand  = brand
        self.name = name
        self.__gears = 5

    def __getGearsInfoStr(self):
        return "gears number " + str(self.__gears)
    
    def printInfo(self):
        print(self.brand, self.name, self.__getGearsInfoStr())

vehicle1 = Vehicle("Doge", "Charger")
# print(vehicle1.__gears) 
# vehicle1.__getGearsInfoStr()
vehicle1.printInfo()
print(vehicle1._Vehicle__gears)
print(vehicle1._Vehicle__getGearsInfoStr())

class Car(Vehicle):
    def __init__(self, brand, name):
        Vehicle.__init__(brand, name)
        # print(self.__getGearsInfoStr())
        print(vehicle1._Vehicle__getGearsInfoStr())

# car1 = Car("Ford", "Mustang")