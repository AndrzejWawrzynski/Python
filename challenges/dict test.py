# 1. Stwórz zmienna config która bedzie stownikiem
#    z konfiguracja strony internetowej, zapisz w niej
#    ponizsze klucze z wartoscia:
#    - "website" z wartoscia "example.com"
#    - "dbType" z wartoscia "mysql"
#    - "dbUser" z wartoscia "admin"
#    - "dbPassword" z wartoscia "12345"
# 2. Pokaz ilosc elementow stownika w konsoli
# 3. Pokaz w konsoli wartosé klucza "dbType" z slownika
# 4. Wykorzystaj petle for in aby przejsé po wszystkich
#    elementach stownika i pokaz je w konsoli wedlug
#    formatu:
#    "Klucz w config: website z wartoscia example.com"

config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassword" : "12345"
}

print("Ilosc elementow slownika:", len(config))

print(config["dbType"])

for i, n in config.items():
    print("Klucz w config: " + i + " z wartoscia: " + n)

