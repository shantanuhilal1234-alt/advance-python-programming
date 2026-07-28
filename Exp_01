class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")



class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron Name: {self.name}")
        print("Borrowed Books:", self.borrowed_books)



class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add a new book
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully!")

    # Register a new patron
    def register_patron(self, name):
        patron = Patron(name)
        self.patrons.append(patron)
        print("Patron registered successfully!")

    # Borrow a book
    def borrow_book(self, patron_name, book_title):
        for patron in self.patrons:
            if patron.name == patron_name:
                for book in self.books:
                    if book.title == book_title and not book.is_borrowed:
                        book.is_borrowed = True
                        patron.borrowed_books.append(book.title)
                        print("Book borrowed successfully!")
                        return
        print("Book not available or Patron not found.")

    # Return a book
    def return_book(self, patron_name, book_title):
        for patron in self.patrons:
            if patron.name == patron_name:
                if book_title in patron.borrowed_books:
                    patron.borrowed_books.remove(book_title)
                    for book in self.books:
                        if book.title == book_title:
                            book.is_borrowed = False
                    print("Book returned successfully!")
                    return
        print("Return failed.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            book.display()


# Main Program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library.add_book(title, author)

    elif choice == "2":
        name = input("Enter Patron Name: ")
        library.register_patron(name)

    elif choice == "3":
        name = input("Enter Patron Name: ")
        title = input("Enter Book Title: ")
        library.borrow_book(name, title)

    elif choice == "4":
        name = input("Enter Patron Name: ")
        title = input("Enter Book Title: ")
        library.return_book(name, title)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")

# Output
'''===== Library Management System =====
1. Add Book
2. Register Patron
3. Borrow Book
4. Return Book
5. Display Books
6. Exit

Enter your choice: 2
Enter Patron Name: Rahul
Patron registered successfully!'''
