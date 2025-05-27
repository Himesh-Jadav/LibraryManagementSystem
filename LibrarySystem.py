class Member:
    def __init__(self, member_id, member_name):
        self.member_id = member_id
        self.member_name = member_name
        self.books_obtained = []

    def __str__(self):
        book_names = ', '.join(book.book_name for book in self.books_obtained)
        return f"{self.member_id}\t{self.member_name}\t{book_names if book_names else "None"}"

class Book:
    def __init__(self, book_id, book_name):
        self.book_id = book_id
        self.book_name = book_name
        self.available_status = True

    def __str__(self):
        return f"{self.book_id}\t{self.book_name}\t{"Available" if self.available_status else "Not Available"}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def addBook(self):
        book_id = int(input("Enter Book Id: "))
        for book in self.books:
            if book.book_id == book_id:
                print(f"Book Id: {book_id}, already exists. Enter different Id")
                break
        else:
            book_name = input("Enter Book Name: ")
            new_book = Book(book_id, book_name)
            self.books.append(new_book)
    
    def addMember(self):
        member_id = int(input("Enter Member Id: "))
        for member in self.members:
            if member.member_id == member_id:
                print(f"Member Id: {member_id}, already exists. Enter different Id")
        else:
            member_name = input("Enter Member Name: ")
            member = Member(member_id, member_name)
            self.members.append(member)

    def deleteBook(self):
        book_id = int(input("Enter Book Id, To be deleted: "))
        count = 0
        for book in self.books:
            if book.book_id == book_id:
                self.books.pop(count)
                print("Deleted Successfully")
                break
            else:
                count += 1
        else:
            print(f"Book with book id: {book_id} does not exists")
        
    def viewBook(self):
        print(f"Book Id\tBook Name\tStatus")
        for book in self.books:
            print(book)

    def deleteMember(self):
        member_id = int(input("Enter Member Id, to be deleted: "))
        count = 0
        for member in self.members:
            if member.member_id == member_id:
                self.members.pop(count)
                print("Deleted Successfully")
                break
            else:
                count+=1
        else:
            print(f"Member with member id: {member_id} not found")

    def viewMember(self):
        print(f"Member Id\tMember Name\tBooks Taken")
        for member in self.members:
            print(member)

    def issueBook(self):
        member_id = int(input("Enter your member id: "))
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            print("Member not found.")
            return
        
        book_id = int(input("Enter Book id: "))
        book = next((b for b in self.books if b.book_id == book_id), None)
        if not book:
            print("Book not found.")
            return
        
        if not book.available_status:
            print("Book is not available.")
            return 
        
        book.available_status = False
        member.books_obtained.append(book)
        print("Book successfully issued.")
        
    def returnBook(self):
        member_id = int(input("Enter Member id: "))
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            print("Member not found.")
            return 
        
        book_id = int(input("Enter Book Id: "))
        book = next((b for b in self.books if b.book_id == book_id), None)
        if not book:
            print("Book not found.")
            return
        
        book.available_status = True
        member.books_obtained.remove(book)
        print("Book returned successfully.")

lib = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. View Book")
    print("4. Add Member")
    print("5. Delete Member")
    print("6. View Member")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. Exit")
    op = int(input("Enter Operation: "))
    if (op == 1):
        lib.addBook()
    elif (op == 2):
        lib.deleteBook()
    elif (op == 3):
        lib.viewBook()
    elif (op == 4):
        lib.addMember()
    elif (op == 5):
        lib.deleteMember()
    elif (op == 6):
        lib.viewMember()
    elif (op == 7):
        lib.issueBook()
    elif (op == 8):
        lib.returnBook()
    elif (op == 9):
        start = False
        print("Exit")
        break
    else:
        print("Invalid Input")
