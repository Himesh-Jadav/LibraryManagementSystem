# 📚 Library Management System

A simple, interactive Library Management System built with Python. This project allows you to manage books and members, issue and return books, and keep track of library resources from the command line.

---

## ✨ Features

- **Book Management:** Add, view, and delete books with ease.
- **Member Management:** Register new members, view member details, and remove members.
- **Issuing & Returning Books:** Issue books to members and track their return.
- **Status Tracking:** See which books are available or issued, and which books each member currently holds.
- **User-Friendly CLI:** Intuitive menu-driven interface for easy navigation.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### How to Run

1. **Clone this repository or copy the code.**
2. Save the code in a file, for example: `library_management.py`
3. Run the script in your terminal:

   ```bash
   python library_management.py
   ```

4. Follow the on-screen menu to manage your library!

---

## 🛠️ Usage

Once you run the script, you'll see a menu like this:

```
--- Library Menu ---
1. Add Book
2. Delete Book
3. View Book
4. Add Member
5. Delete Member
6. View Member
7. Issue Book
8. Return Book
9. Exit
Enter Operation:
```

Choose an option by entering the corresponding number.

---

## 📦 Main Classes & Structure

- **Member:** Represents a library member and tracks books they've borrowed.
- **Book:** Represents a book and its availability status.
- **Library:** Main class that manages books, members, issuing and returning of books.

---

## 📝 Example

```plaintext
--- Library Menu ---
1. Add Book
2. Delete Book
3. View Book
4. Add Member
5. Delete Member
6. View Member
7. Issue Book
8. Return Book
9. Exit
Enter Operation: 1
Enter Book Id: 101
Enter Book Name: Python Basics
Book added successfully!
```

---

## 💡 Notes

- The system uses a simple in-memory list to store books and members (no database required).
- All operations are performed via the command line.
- Each book and member must have a unique ID.

---

## 🤝 Contributing

Feel free to fork the project and open pull requests! Suggestions and improvements are always welcome.

---

## 🧑‍💻 Author

**Himesh Jadav**

- [GitHub](https://github.com/Himesh-Jadav)

---

Enjoy managing your library! 📖
