
class Car:
    def __init__(self, brand, name, color, year):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year
        self.mileage = 1
        self.setTopSpeed(100)
        self.printInfo()

    def printInfo(self):
        print(self.brand, self.name, 
              self.color, self.year, self.mileage, self.topSpeed)

    def setTopSpeed(self, newtopSpeed):
        self.topSpeed = newtopSpeed

mustang = Car("Ford", "Mustang", "red", 1970)
mustang.mileage = 500
mustang.setTopSpeed(235)
# mustang.topSpeed = 230
# mustang.printInfo()
# print(mustang.topSpeed)
mustang.printInfo()

charger = Car("Doge", "Charger", "blue", 1971)
charger.setTopSpeed(232)
charger.printInfo()