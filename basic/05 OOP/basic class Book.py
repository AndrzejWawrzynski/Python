
class Book:
    def __init__(self, author, title = "unknown", isbn = "unknown", year = "unknown"):
        self.author  = author
        self.title  = title
        self.isbn = isbn
        self.year = year

    def printData(self):
        print(self.author, self.title, self.isbn, self.year)

book1 = Book("Ania Kowalska", "title", "isbn", 2024)
book1.printData()

book2 = Book("Adam", year = 2022)
book2.printData()