from abc import ABC,abstractmethod

class Book(ABC):
    def __int__(self,title,author):
        self.title=title
        self.author=author

    @abstractmethod
    def display():
        pass

class MyBook(Book):
    def __int__(self,title,author,price):
        super().__int__(title, author)
        self.price=price

    def display(self):
        print("Title: ",title)
        print("Author: ",author)
        print("Price: ",price)

title = input("The Alchemist")
author = input("Paulo Coelheo")
price =int(input("248"))
obj=MyBook()
obj.display()

