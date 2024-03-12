from cart import *

phone1 = Phone("Phone X", 1000, "red")
phone2 = Phone("Phone Z", 2000, "blue")
phone3 = Phone("Phone S", 1500, "black")
tv1 = TV("TV 1", 2000, 55)
tv2 = TV("TV 2", 3000, 85)
tv3 = TV("TV 3", 2500, 65)

cart = Cart()
cart.addProduct(tv1)
cart.addProduct(tv2)
cart.addProduct(tv3)
cart.addProduct(phone1)
cart.addProduct(phone2)
cart.addProduct(phone3)
cart.addProduct("test")
print(cart)