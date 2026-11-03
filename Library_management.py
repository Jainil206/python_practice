
books = [
    {"id": 101, "name": "Python", "author": "Guido", "quantity": 5},
    {"id": 102, "name": "Java", "author": "James", "quantity": 3},
    {"id": 103, "name": "C Programming", "author": "Dennis", "quantity": 4}
]


def add_book():
    book_id = int(input("Enter Book ID: "))

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists!")
            return

    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))

    if name == "" or author == "" or quantity < 0:
        print("Enter valid book details!")
        return

    book = {
        "id": book_id,
        "name": name,
        "author": author,
        "quantity": quantity
    }

    books.append(book)
    print("Book added successfully!")


def display_books():
    if len(books) == 0:
        print("Library is empty!")
        return

    print("\n----------- LIBRARY BOOKS -----------")
    print("ID\tName\t\tAuthor\t\tQuantity")

    for book in books:
        print(
            book["id"], "\t",
            book["name"], "\t\t",
            book["author"], "\t\t",
            book["quantity"]
        )


def search_book():
    book_id = int(input("Enter Book ID to search: "))

    for book in books:
        if book["id"] == book_id:
            print("\nBook Found!")
            print("ID:", book["id"])
            print("Name:", book["name"])
            print("Author:", book["author"])
            print("Available Quantity:", book["quantity"])
            return

    print("Book not found!")


def update_book():
    book_id = int(input("Enter Book ID to update: "))

    for book in books:
        if book["id"] == book_id:
            print("1. Update Book Name")
            print("2. Update Author Name")
            print("3. Update Quantity")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter new book name: ")

                if name != "":
                    book["name"] = name
                    print("Book name updated successfully!")
                else:
                    print("Book name cannot be empty!")

            elif choice == "2":
                author = input("Enter new author name: ")

                if author != "":
                    book["author"] = author
                    print("Author updated successfully!")
                else:
                    print("Author name cannot be empty!")

            elif choice == "3":
                quantity = int(input("Enter new quantity: "))

                if quantity >= 0:
                    book["quantity"] = quantity
                    print("Quantity updated successfully!")
                else:
                    print("Quantity cannot be negative!")

            else:
                print("Invalid choice!")

            return

    print("Book not found!")


def delete_book():
    book_id = int(input("Enter Book ID to delete: "))

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book deleted successfully!")
            return

    print("Book not found!")


def issue_book():
    book_id = int(input("Enter Book ID to issue: "))

    for book in books:
        if book["id"] == book_id:
            if book["quantity"] > 0:
                book["quantity"] -= 1
                print("Book issued successfully!")
            else:
                print("Book is not available!")
            return

    print("Book not found!")


def return_book():
    book_id = int(input("Enter Book ID to return: "))

    for book in books:
        if book["id"] == book_id:
            book["quantity"] += 1
            print("Book returned successfully!")
            return

    print("Book not found!")


while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        issue_book()

    elif choice == "7":
        return_book()

    elif choice == "8":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
