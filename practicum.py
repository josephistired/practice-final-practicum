"""
Implement your solution to the practicum in this file.

@author Joseph Carmosino
"""
class Book:
  __slots__ = ["__title", "__author", "__publication_year"]
  
  def __init__(self, title, author, publication_year):
    self.__title = title
    self.__author = author
    self.__publication_year = publication_year
    
  def getTitle(self):
    return self.__title
  
  def getAuthor(self):
    return self.__author
  
  def getPublicationYear(self):
    return self.__publication_year
  
  def __str__(self):
    return str(self.getTitle()) + " by " + str(self.getAuthor()) + " (" + str(self.getPublicationYear()) + ")"
  
  def __repr__(self):
    return str(self.getTitle()) + ", " + "a book by " + str(self.getAuthor()) + ", " + "published in " + str(self.getPublicationYear()) + "."
  
  def __lt__(self, other):
    return self.getAuthor() < other.getAuthor()
  
  def __gt__(self, other):
    return self.getAuthor() > other.getAuthor()
  
  def __eq__(self, other):
    return self.getAuthor() == other.getAuthor()
    
class Library:
  __slots__ = ["__name", "__books"]
  
  def __init__(self, name):
    self.__name = name
    self.__books = []
  
  def getName(self):
    return self.__name
  
  def getBooks(self):
    return self.__books
  
  def is_empty(self):
    if len(self.getBooks()) == 0:
      return True
    else:
      return False
    
  def reload(self, books):  
    for book in books:
      self.__books.append(book)
  
  def check_out(self, title, author):
    for book in self.getBooks():
      if book.getTitle() == title and book.getAuthor() == author:
        book = self.__books.remove(book)
        return book
      else:
        return None
        
  def return_book(self, book):
    self.__books.append(book)

def organize_library(library:Library) -> None:
   books = Library.getBooks(library)
   new_order = []
   
   for book in books:
     new_order.append(book)
     
   new_order.sort()
   
   Library.reload(library, new_order)
   

def main():
    """
    Use this function to manually test your code (if needed)
    """

if __name__ == "__main__":
    main()
