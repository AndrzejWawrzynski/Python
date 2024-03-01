#
# Funkcja z domyslnymi wartosciami parametrow
# 1) Napisz funkcje z parametrami:
#    - email
#    - country z domysina wartoscia "Polska"
#    - company z domysina wartoscia "Example Ltd"
# 2) Zwroc z funkcji stownik z elementami jako parametry
# 3) Pretestuj funkcje z jednym argumentem ola@example.com
#    oraz drugi przypadek z kasia@example.com bedaca z UK

def user(email, country = "Polska", company = "Example Ltd"):
    return {
        "email" : email,
        "country" : country,
        "company" : company
    }

print(user("ola@example.com"))
print(user("kasia@example.com", "UK"))
print(user("adam@example.com", "DE", "Test LTD"))