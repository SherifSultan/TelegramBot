import requests

API_URLget = "https://demo.api-platform.com/books?page=1&itemsPerPage=10"
API_URLpost = 'https://demo.api-platform.com/books'


def get_books():
    """Retrieves books data from an API using a GET request
     if the request is successful, otherwise returns None.
     It retrieves only 10 books as been set in the declared (API_URLget)"""

    response = requests.get(API_URLget)
    if response.status_code == 200:
        data = response.json()
        return data['hydra:member']
    else:
        return None


def format_books(books, flag):
    """list of books by concatenating the title and optionally the author if the flag is True,
     returning the formatted string. If no books are present, it returns No books found."""

    if not books:
        return "No books found."

    formatted_books = ""
    for book in books:
        title = book['title']
        author = book['author']
        formatted_books += f"Title: {title} "+(("Author: " + author) if flag else "") + "\n"

    return formatted_books


def add_book(title, author):
    """Adds a book to the API using a POST request
    and returns a success message with the book ID if successful,
    otherwise prints the error message and returns Error."""

    bookData = {'title': title, 'author': author, 'description': 'string', 'publicationDate': '2023-07-20T18:11:08.904Z'}
    adder = requests.post(API_URLpost, json=bookData)

    if adder.ok:
        return 'Book added ' + ' Book ID ' + adder.json()['id']
    else:
        return 'Error'


def print_books():
    """Retrieves books data, formats it without displaying the author, and returns the formatted books"""

    return format_books(get_books(), False)


def search_books(id):
    """function searches for a book using its ID, formats the book's data (including the author)
    and returns it if found, otherwise returns Book not found."""

    adder = requests.get(API_URLpost + '/' + id)
    if adder.status_code == 200:
        data = adder.json()
        return format_books([data], True)
    else:
        return 'Book not found'

