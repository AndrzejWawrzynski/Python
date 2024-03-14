import os

print("Current working directory :", os.getcwd())

files = os.listdir(".")
print("----------")
print(files)

files = os.listdir("./programs")
print("----------")
print(files)

files = os.listdir("./basic/05 OOP/cart")
print("----------")
print(files)

files = os.listdir("..")
print("----------")
print(files)

files = os.listdir("../Music")
print("----------")
print(files)