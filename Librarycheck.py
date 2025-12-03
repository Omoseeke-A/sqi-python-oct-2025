library = []

def add_book():
    """Add a new book to the library."""
    for book in library:
        if book["Author"] == author:
            print(f"book by {author} already exist")
            return
        
    title = input("Enter a book title: ").title()
    author = input("Enter author's name: ").lower()
    year = int(input("Enter year of publication: "))
    isbn = int(input("Enter the ISBN number: "))
    available = True

        
    new_book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "ISBN": isbn,
        "Available": available
 }

    library.append(new_book)
    print(f"The Book {title} by {author} added successfully.")


def view_books():
    """Display all the books in the library."""
    if not library:
        return "The book is not in the Library"
    return library
    
def update_book(isbn):
    """Update the information of a book given its ISBN."""
    for book in library:
        if book["ISBN"]  == isbn:
            print("Enter new details (leave blank to keep current values): ")
            title = input(f"Title ({book['Title']}): ") or book["Title"]
            author = input(f"Author ({book['Author']}): ") or book["Author"]
            year = input(f"Year ({book['Year']}): ")
            year = int(year) if year else book["Year"]
            book.update({"Title": title, "Author": author, "Year": year})
            print("Book updated successfully!")
    return
    print("Book not found.")

def delete_book(isbn):
    """Remove a book from the library using its ISBN."""
    for book in library:
        if book["ISBN"] == isbn:
            library.remove(book)
            print(f"The book with ISBN {isbn} deleted succefully.")
            return
    print("Book not found")

def search_book(title: str):
    """Search for a book by its exact title."""
    for book in library:
        if book["Title"].lower() == title.lower():
             print(
                f"Found: Title: {book['Title']}, Author: {book['Author']}, "
                f"Year: {book['Year']}, ISBN: {book['ISBN']}, "
                f"Available: {'Yes' if book['Available'] else 'No'}"
            )
        return
    print("Book not found.")

def borrow_book(isbn):
    """Mark a book as borrowed (not available)."""
    for book in library:
        if book["ISBN"] == isbn:
            if book["Available"]:
                book["Available"] = False
                print(f"You borrowed '{book['Title']}'.")
            else:
                print("Book is already borrowed.")
            return
    print("Book not found.")


def return_book(isbn):
    """Mark a book as returned (available)."""
    for book in library:
        if book["ISBN"] == isbn:
            if not book["Available"]:
                book["Available"] = True
                print(f"You returned '{book['Title']}'.")

            else:
                print("Book was not borrowed.")
                return
                print("Book not found.")

menu = """
............LIBRARY MENU................
1. add_book
2. view_books
3. update_book 
4. delete_book
5. search_book
6. borrow_book
7. return_book
8. Exit
"""

while True:
    print(menu)
    choice = input("Choose an option of what you want to do in the library today: ")

    if choice not in ("1", "2", "3", "4", "5", "6", "7", "8"):
        print("Invalid entry, please choose another option: ")
    elif choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        isbn = input("Enter ISBN of book to update: ")
        update_book(isbn)
    elif choice == "4":
        isbn = input("Enter the ISBN of the book you wish to delete: ")
        delete_book(isbn)
    elif choice == "5":
        title = input("Enter the title of the book you are seearching for: ")
        search_book(title)
    elif choice == "6":
        isbn = input("Enter the ISBN of the book you wish to borrow: ")
        borrow_book(isbn)
    elif choice == "7":
        isbn = input("Enter the ISBN of the book you wish to return: ")
        return_book(isbn)
    elif choice == "8":
        print("Goobye thanks for coming")
        break
if name == "_main_":
    print( menu())