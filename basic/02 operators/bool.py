# AND

print ( True and True ) # zwraca True
print ( True and False ) # zwraca False
print ( False and False ) # wraca False
print ( 8 > 3 and 3 == 3 ) # True bo obie strony zwracaja True
print ( 4 > 4 and 1 >= 10 ) # False
print ( 10 == 5 and 3 < 1 ) # False

if 5 == 5 and 10 > 4:
    print ("True bo oba warunki spelnione")

taskCompleted = True
linesOfCodeWritten = 100
if taskCompleted == True and linesOfCodeWritten >= 50:
    print("Go home")  

hourOfDay = 15
if taskCompleted == True and linesOfCodeWritten >= 60 and hourOfDay >= 15:
    print ("Go home")

# OR

print ( True or True ) # True
print ( True or False ) # True
print ( False or False ) # False
print ( 10 > 1 or 7 == 7 ) # True
print ( 3 < 5 or 1 > 3) # True
print ( 10 == 11 or 2 < 1) # False

if "Ania" == "Ania" or 10 == 1:
    print ("Ania to Ania")

if 10 > 5 or "Ania" != "Ola":
    print(" true or true ")

if 3 == 5 or "Ania" == "Ola":
    print(" false or false " )

# NOT

print ( not True ) # False
print ( not False ) # True
print ( not ( 10 == 10) ) # False
print ( not ( 4 < 1) ) # True
print ( not ( 5 == 5 and 3 > 1 ) ) # False

taskCompleted = False # zadanie nie bylo skonczone
if not taskCompleted:
    print ("Zadanie nie zostalo wykonane")  

taskCompleted = False

if taskCompleted == True:
    print("Go home")

if not taskCompleted:
    print("Stay a bit longer and finish")

