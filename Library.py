# Project Overview:
# Create a simple library management system where users can add, view, update, and delete 
# books in a file named `the_librarian.py`.
# Requirements:
# Data Storage: Use a list of dictionaries to store book information. Each book should have the following attributes:
# Title (string)
# Author (string)
# Year of publication (int)
# ISBN (string)
# Available (boolean)
# Functions/Actions:
# add_book(): Add a new book to the library.
# view_books(): Display all the books in the library.
# update_book(isbn): Update the information of a book given its ISBN.
# delete_book(isbn): Remove a book from the library using its ISBN.
# search_book(title): Search for a book by its exact title.
# borrow_book(isbn): Mark a book as borrowed (not available).
# return_book(isbn): Mark a book as returned (available).
# User Interface: Use a loop to display a menu and prompt the user for an action above until they choose to exit.
#  Assume the user always inputs the correct data types.

library = []
class Operations:

    def __init__(self,title,author,year,isbn,availablility ):
        self.title = title
        self.author = author
        self.year= year
        self.isbn = isbn
        self.availability = availablility
        self.book = []
        

    def add_book(self,book:list):
        
        book = [
            title == input("What is the title?: "),
            author== input("Who is the Author?: "),
            year ==int (input("What year was it published?: ")),
            isbn == input("What is the isbn?: "),
            availability == input("Is it available?:")
            ]
        library.append({"Title": title,"Author": author,"year": year,"ISBN":isbn,"Avaialability":availability})

        print(f"{library}has been added")    
    def view_books():
        return (library)
    def update_books:
    

choice = input("What operation are you performing? : ")
if choice == "add_book":
    
        title = input("What is the title?: "),
        author:= input("Who is the Author?: "),
        year :=int (input("What year was it published?: ")),
        isbn := input("What is the isbn?: "),
        availability := input("Is it available?:")
    library.append({"Title": title,"Author": author,"year": year,"ISBN":isbn,"Avaialability":availability})
    print(f"{library}has been added")
        
if choice in "view_books":
    print(f"{Operations.view_books()}")
if choice in "update_books":
    print(update_book)
#     
# elif choice in "delete_books":
#     delete_books()
# elif choice in "search_books":
#     search_books()
# elif choice in "borrow_books":
#     borrow_books()
# elif choice in "return_books":
#     return_books()
    
    

# title = input("What is the title?: ")

# Authour = input("Who is the Author?: ")

# Year=int (input("What year was it published?: "))
# isbn = input("What is the isbn?: ")
# availability = input("Is it available?:")