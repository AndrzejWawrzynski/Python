# Zadanie - klasa do tworzenia pizzy
# Stworzysz teraz prosta klase Pizza, ktora pozwoli na tworzenie
# obiektu pizzy z lista skladnikow.
#
# 1) Zdefiniuj klase Pizza z konstruktorem (_init_), ktory tworzy
#    atrybut 'ingredients' (skladniki), bedacy pusta lista na start.
# 2) Dodaj metode 'addIngredient', ktora przyjmuje jeden parametr
#    (oprocz self) - skladnik (ingredient) do dodania do pizzy.
#    Sprawdz, czy skiadnik jest typu str, jesli tak - dodaj go do listy.
# 3) Dodaj metode 'showIngredients', ktora wyswietla wszystkie
#    skiadniki pizzy.
# 4) Stworz instancje klasy Pizza.
# 5) Dodaj skladniki do pizzy uzywajac metody "addIngredient' :
#    "ser", "pomidor", "pieczarki"
# 6) Wyswietl skladniki pizzy wywolujac metode " showIngredients

class Pizza:
    def __init__(self) -> None:
        self.ingredients = []
    
    def addIngredient(self, ingredients):
        if isinstance(ingredients, str):
            self.ingredients.append(ingredients)
        else:
            print("Nieprawidlowe dane")

    def showIngredients(self):
        print("Skladniki :",self.ingredients)

pizza = Pizza()
pizza.addIngredient("ser")
pizza.addIngredient("pomidor")
pizza.addIngredient("pieczarki")

pizza.showIngredients()
