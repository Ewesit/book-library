# Here's an implementation of the Book and Library classes 

#create a book class that represents a book in the library
class Book:
    def __init__(self, title, author, isbn): #constructor method, 
        #__init__  this method is called automatically to initialize the object.
        #self: This is a reference to the current instance of the class. 
        #self: It is used to access variables and methods of the class within the class definition.
        # Initialize a Book object with title, author, and ISBN
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False  # Initially, the book is not checked out

    def check_out(self):
        # Check out the book if it is not already checked out
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"Book '{self.title}' by {self.author} has been checked out.")
        else:
            print(f"Book '{self.title}' by {self.author} is already checked out.")

    def return_book(self):
        # Return the book if it is checked out
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"Book '{self.title}' by {self.author} has been returned.")
        else:
            print(f"Book '{self.title}' by {self.author} is not checked out.")

    def __str__(self):
        # String representation of the book
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Checked Out: {self.is_checked_out}"


class Library:
    def __init__(self):
        # Initialize the library with an empty list of books
        self.books = []

    def add_book(self, book):
        # Add a Book object to the library's book list
        self.books.append(book)

    def remove_book(self, isbn):
        # Remove a book from the library by ISBN
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN {isbn} has been removed.")
                return
        print(f"Book with ISBN {isbn} not found.")

    def check_out_book(self, isbn):
        # Check out a book by ISBN
        for book in self.books:
            if book.isbn == isbn:
                book.check_out()
                return
        print(f"Book with ISBN {isbn} not found.")

    def return_book(self, isbn):
        # Return a book by ISBN
        for book in self.books:
            if book.isbn == isbn:
                book.return_book()
                return
        print(f"Book with ISBN {isbn} not found.")

    def list_books(self):
        # List all books in the library
        print("Books in the library:")
        for book in self.books:
            print(book)


# Demonstration
library = Library()

# Adding books to the library
library.add_book(Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "9780590353403"))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "9780061120084"))
library.add_book(Book("1984", "George Orwell", "9780451524935"))
library.add_book(Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488"))

# Checking out a couple of books
library.check_out_book("9780590353403")
library.check_out_book("9780743273565")

# Listing all books in the library
library.list_books()

# Returning a book
library.return_book("9780590353403")

# Listing all books again
library.list_books()
