class Book:
    def __init__(self, title, author, pages):
        print("Book has been created")
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f'Naslov: {self.title}, Autor: {self.author}, Broj stranica: {self.pages}'
    def __len__(self):
        return self.pages
    def __del__(self):
        print("Book has been deleted")


book = Book("Uvod u programiranje", "Marko Markovic", 240)

lista = [1, 2, 3]
print(lista) # kako Python zna kako da stampa listu?
print(book)
print(len(book))
del book
