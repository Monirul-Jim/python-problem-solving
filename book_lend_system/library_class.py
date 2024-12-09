class Library:
    _book_list = []

    @classmethod
    def entry_book(cls, book):
        cls._book_list.append(book)

    @classmethod
    def view_all_books(cls):
        if not cls._book_list:
            print("No books available in the library.")
        else:
            for book in cls._book_list:
                book.view_book_info()

    @classmethod
    def find_book(cls, book_id):
        """Finds a book by its ID."""
        for book in cls._book_list:
            if book._book_id == book_id:
                return book
        return None


class Book:
    def __init__(self, book_id, title, author):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._availability = True
        Library.entry_book(self)

    def borrow_book(self):
        if self._availability:
            self._availability = False
            print(f"You have successfully borrowed '{self._title}'.")
        else:
            print(f"The book '{self._title}' is currently unavailable.")

    def return_book(self):
        if not self._availability:
            self._availability = True
            print(f"You have successfully returned '{self._title}'.")
        else:
            print(f"The book '{self._title}' was not borrowed.")

    def view_book_info(self):
        availability_status = "Available" if self._availability else "Not Available"
        print(
            f"ID: {self._book_id}, Title: '{self._title}', Author: {self._author}, Status: {availability_status}")


def main():
    Book("100", "Introduction to Python Programming", "Guido van Rossum")
    Book("101", "Introduction to C++", "Bjarne Stroustrup")
    Book("102", "Javascript & Modern Web", "Brendan Eich")
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            Library.view_all_books()

        elif choice == "2":
            book_id = input("Enter the book ID to borrow: ")
            book = Library.find_book(book_id)
            if book:
                book.borrow_book()
            else:
                print(f"No book found with ID '{book_id}'.")

        elif choice == "3":
            book_id = input("Enter the book ID to return: ")
            book = Library.find_book(book_id)
            if book:
                book.return_book()
            else:
                print(f"No book found with ID '{book_id}'.")

        elif choice == "4":
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
