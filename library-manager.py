import json  # For reading and writing JSON data
import os  # For checking if the file exists
import time  # For adding delays

# File to store library data
DATA_FILE = 'library.txt'

# Function to load library data from the file
def load_library():
    if os.path.exists(DATA_FILE):  # Check if the file exists
        try:
            with open(DATA_FILE, 'r') as file:  # Open the file in read mode
                return json.load(file)  # Load the data as a list of dictionaries
        except (json.JSONDecodeError, IOError):  # Handle errors
            print("Error: Unable to load library data. Starting with an empty library.")
    return []  # Return an empty list if the file doesn't exist or has errors

# Function to save library data to the file
def save_library(library):
    try:
        with open(DATA_FILE, 'w') as file:  # Open the file in write mode
            json.dump(library, file, indent=4)  # Save the data in JSON format
    except IOError:  # Handle errors
        print("Error: Unable to save library data.")

# Function to add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"

    # Create a dictionary for the book
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    # Add the book to the library
    library.append(book)
    save_library(library)  # Save the updated library to the file
    print(f"Book '{title}' added successfully!")
    time.sleep(5)  # Wait for 5 seconds before showing the menu again

# Function to remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")

    # Find and remove the book
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)  # Save the updated library to the file
            print(f"Book '{title}' removed successfully!")
            time.sleep(5)  # Wait for 5 seconds before showing the menu again
            return

    print(f"Book '{title}' not found in the library.")
    time.sleep(5)  # Wait for 5 seconds before showing the menu again

# Function to search for a book
def search_book(library):
    search_term = input("Enter the title or author to search: ").lower()

    # Search for matching books
    results = []
    for book in library:
        if search_term in book["title"].lower() or search_term in book["author"].lower():
            results.append(book)

    # Display results
    if results:
        print("Matching Books:")
        for book in results:
            status = "Read" if book["read"] else "Unread"
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {status}")
    else:
        print("No matching books found.")
    time.sleep(5)  # Wait for 5 seconds before showing the menu again

# Function to display all books
def display_books(library):
    if not library:
        print("No books in the library.")
    else:
        print("Your Library:")
        for book in library:
            status = "Read" if book["read"] else "Unread"
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {status}")
    time.sleep(5)  # Wait for 5 seconds before showing the menu again

# Function to display statistics
def display_stats(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percentage_read:.2f}%")
    time.sleep(5)  # Wait for 5 seconds before showing the menu again

# Main menu
def main():
    library = load_library()  # Load library data from the file
    print("\nWelcome to your Personal Library Manager!")

    while True:
        print("\n--- Menu ---")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)  # Save library data before exiting
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)  # Wait for 2 seconds for invalid choices

# Run the program
if __name__ == "__main__":
    main()