# Personal Library Manager

A simple command-line application to manage your book collection. This program allows you to add, remove, search, and display books, as well as view basic statistics about your library.

---

## Features

- **Add a Book**: Add a new book to your library with details like title, author, publication year, genre, and read status.
- **Remove a Book**: Remove a book from your library by its title.
- **Search for a Book**: Search for books by title or author.
- **Display All Books**: View all books in your library in a formatted list.
- **Display Statistics**: See the total number of books, the number of books read, and the percentage of books read.
- **Save and Load Library**: Automatically save your library to a file (`library.txt`) and load it when the program starts.

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/personal-library-manager.git
   cd personal-library-manager
   ```

2. **Run the Program**:
   ```bash
   python library_manager.py
   ```

3. **Follow the Menu**:
   - The program will display a menu with options to add, remove, search, display, and view statistics.
   - Enter the number corresponding to your choice and follow the prompts.

4. **Exit the Program**:
   - Choose the "Exit" option to save your library and exit the program.

---

## File Structure

- `library_manager.py`: The main Python script for the Personal Library Manager.
- `library.txt`: A JSON file that stores your library data. It is automatically created and updated by the program.

---

## Code Overview

### Key Functions

- **`add_book()`**: Adds a new book to the library.
- **`remove_book()`**: Removes a book from the library by its title.
- **`search_book()`**: Searches for books by title or author.
- **`display_books()`**: Displays all books in the library.
- **`display_stats()`**: Displays library statistics (total books, books read, percentage read).
- **`load_library()`**: Loads the library data from `library.txt`.
- **`save_library()`**: Saves the library data to `library.txt`.

### Example Data in `library.txt`

```json
[
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": "1925",
        "genre": "Fiction",
        "read": true
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": "1949",
        "genre": "Dystopian",
        "read": false
    }
]
```

---

## Requirements

- Python 3.x
- No external libraries are required.

---

## How It Works

1. **Loading Data**:
   - When the program starts, it loads the library data from `library.txt` (if the file exists).
   - If the file doesn't exist, it starts with an empty library.

2. **Saving Data**:
   - Whenever a book is added or removed, the program saves the updated library to `library.txt`.

3. **User Interaction**:
   - The program uses a simple menu system to interact with the user.
   - After each action, the program waits for 5 seconds to give the user time to read the output.

---

## Example Usage

### Add a Book
```
Enter the book title: The Great Gatsby
Enter the author: F. Scott Fitzgerald
Enter the publication year: 1925
Enter the genre: Fiction
Have you read this book? (yes/no): yes
Book 'The Great Gatsby' added successfully!
```

### Display All Books
```
Your Library:
1. The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read
2. 1984 by George Orwell (1949) - Dystopian - Unread
```

### Display Statistics
```
Total books: 2
Books read: 1
Percentage read: 50.00%
```

---

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Here are some ideas for improvements:
- Add support for sorting books by title, author, or year.
- Implement a feature to edit book details.
- Add a graphical user interface (GUI).

---



## Author

- **Your Name**
- GitHub: [bilalchandio1]((https://github.com/bilalchandio1)))
- Email: ahchandio21@gmail.com

---

Enjoy managing personal library with this simple and efficient tool! 😊

---

 😊
