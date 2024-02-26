
num = 0
operation = None
reset = True
result = None
calcOperation = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int(input("Podaj liczbe startowa:"))
        reset = False

    operation = input("Podaj operacje arytmetyczna jak np: "
                      + str(calcOperation) + " lub exit jesli koniec lub reset: ")
    if operation == "exit":break
    if operation == "reset":
        reset = True
        continue
    if not operation in calcOperation:
        print("Wprowadzona zostala bledna operacja.")
        continue
    secondNum = int(input("Podaj druga liczbe:"))

    if operation == "+":
        result = num + secondNum

    if operation == "-":
        result = num - secondNum

    if operation == "*":
        result = num * secondNum

    if operation == "/":
        result = num / secondNum

    if operation == "**":
        result = num ** secondNum

    print("Wynik operacji " + str(num) + " " + str(operation) + " " 
          + str(secondNum) + " = " + str(result))
    
    num = result
    result = None