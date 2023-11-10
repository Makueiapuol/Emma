class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            return f"Checked out: {self.title}"
        else:
            return f"{self.title} is not available for checkout."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"Returned: {self.title}"
        else:
            return f"This book is already available in the library."

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.publication_year}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def __str__(self):
        return f"Member Name: {self.name}\nMember ID: {self.member_id}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return f"Removed: {book.title} from the library."
        else:
            return f"{book.title} is not in the library."

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            return f"Removed: {member.name} from the library members."
        else:
            return f"{member.name} is not a member of the library."

    def display_books(self):
        return "\n".join([str(book) for book in self.books])

    def display_members(self):
        return "\n".join([str(member) for member in self.members])


# Example of how to use the library system

# Create books
book1 = Book("The Human Tide", "Paul Morland", 1925)
book2 = Book("Gifted Hands", "Ben Carson", 1960)
book3 = Book("The Dopamine Nation", "Dr. Anna Lembke", 1949)

# Create members
member1 = Member("Aman Teresa", 101)
member2 = Member("Kazibwe Trevor", 102)

# Create the library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Add members to the library
library.add_member(member1)
library.add_member(member2)

# Display books and members
print("Books in the library:")
print(library.display_books())

print("\nMembers of the library:")
print(library.display_members())

# Member checks out a book
print(member1.name, "tries to check out", book1.title)
print(book1.check_out())

# Member tries to check out an already checked out book
print(member2.name, "tries to check out", book1.title)
print(book1.check_out())

# Member returns a book
print(member1.name, "tries to return", book1.title)
print(book1.return_book())

# Display books in the library after check-out and return
print("\nBooks in the library:")
print(library.display_books())

# Remove a member from the library
print("\nRemoving member", member2.name)
print(library.remove_member(member2))

# Display members after removing one
print("\nMembers of the library:")
print(library.display_members())

# Remove a book from the library
print("\nRemoving book", book3.title)
print(library.remove_book(book3))

# Display books after removing one
print("\nBooks in the library:")
print(library.display_books())
