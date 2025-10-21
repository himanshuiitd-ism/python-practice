# Aggregation = Represents a relationship where one obj (the whole) contains refresences to one or more independent obj(the parts)

class Library:
  def __init__(self,name):
    self.name = name
    self.books = []  #this is ref from other class
  
  def add_book(self,book):
    self.books.append(book)

  def list_book(self):
    return [f"{book.title} by {book.author}" for book in self.books]

class Book:
  def __init__(self,title,author):
    self.title = title
    self.author = author

library = Library("Indian Public Library")
book1= Book("Harry Potter","JK Rollins")
book2= Book("The color of magic","Terry Pratchet")

library.add_book(book1)
library.add_book(book2)

print(library.name)
for book in library.list_book():
  print(book)