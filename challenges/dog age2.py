
def calculateHumanYears (dogYears) :
    if dogYears <= 2:
        return dogYears * 10.5
    else:
        return 21 + (dogYears - 2) * 4

while True:
    dogAge = float(input ("Wrowadz wiek psa w latach:"))
    humanYears = calculateHumanYears(dogAge)
    print("Wiek psa w ludzkich latach:", humanYears)
    
    again = input("Czy chcesz obliczy wiek innego psa? (tak/nie):")
    if again.lower() != "tak":
        break