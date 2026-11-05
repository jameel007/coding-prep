class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
    
    def addbooks(self,book):
        self.books.append(book)
    
    def listbooks(self):
        return [f"{book.book} by {book.author}" for book in self.books]

class Book:
    def __init__(self,book,author):
        self.book = book
        self.author = author


library = Library("Newyork Public Library") 

book1 = Book("Harry Potter","J.K Rowling")
book2 = Book("The Alchemist","Paulo")
book3 = Book("Essentialism","J")

library.addbooks(book1)
library.addbooks(book2)
library.addbooks(book3)

print(library.name)

for books in library.listbooks():
    print(books)

print(dir(Book))