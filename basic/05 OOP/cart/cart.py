from product import *

class Cart:
    def __init__(self):
        self.__productsList = []
        self.__cartValue = 0

    def addProduct(self, product):
        # if isinstance(product, Phone) or isinstance(product, TV):
        if isinstance(product, Product):
            if product not in self.__productsList:
                self.__productsList.append(product)
                self.calculateCart()

    def calculateCart(self):
        self.__cartValue = 0
        for i in self.__productsList:
            self.__cartValue += i.price

    def __str__(self):
        strData = "\nCar info, product list:"
        for i in self.__productsList:
            strData += "\n - " + str(i.name) + " " + str(i.price)
        strData += "\n cart value:" + " " + str(self.__cartValue)
        return strData
