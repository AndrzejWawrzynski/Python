
print("Hello " + "World")
print("Hello " * 3)

string = "Hello World!"
print (string[0]) # H
print (string[0:5]) # Hello

print("Hello" in string) # True
print("Hello" not in string) # False

multiline = """ line 1
line 2
line 3
"""

print("ala".capitalize())
print("Ola ma kota, Ola ma psa".count("Ola"))
print(len("Ola ma kota, Ola ma psa"))

print("Hello".center(20, "*"))

print(string.startswith("Hello"))
print(string.endswith("World!"))

print(string.find("Ola"))
print(string.find("World"))

print("Ola ma psa, Ola ma kota".rfind("Ola"))

print("12341234".isalnum()) # True
print("12341234.".isalnum()) # False
print("12341234 k".isalnum()) # False

print("12341234 k".isalpha()) # False
print(" kot".isalpha()) # False
print("kot".isalpha()) # True
print("kot 2".isalpha()) # False

print("test".islower())
print("tesT".islower())
print("TEST".isupper())
print("TEST".isspace())
print("   \n\t".isspace())

print("-|".join(["Ala","Ola","Adam"]))

print("Hello World".lower())
print("Hello World".upper())
print("Hello World".swapcase())

print("   \n\t Hello World \n\t  ".lstrip())
print("   \n\t Hello World \n\t  ".rstrip())
print("   \n\t Hello World \n\t  ".strip())
print("   \n\t Hello     World \n\t  ".strip())

print("Ola ma psa, Ola ma kota".replace("Ola", "Kasia"))

print("My name is {myName}, I am from {country}".format(myName = "Kuba", country = "Poland"))
print("My name is {myName}, my postal code is {code}".format(myName = "Kuba", code = 81112))
print("My name is {0}, my postal code is {1}".format("Kuba", 81112))
print("My name is {}, my postal code is {}".format("Kuba", 81112))


