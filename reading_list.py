"""A program that can store and display books from a user's reading list
mini-project from Teclado"""


def add_book():
    book_title = input("Book title :    ").strip().title()
    author_name = input("Author's name: ").strip().title()
    year_of_publication = int(input("Publication's year:    ").strip())

    print("\n... your book is added")

    return book_title, author_name, year_of_publication


def show_books(books_store):
    print()
    for counter, (title, name, year) in enumerate(books_store, start=1):
        print(f'{counter}. {title} by {name} ({year})')


menu = """Please choose an operation
A: add a book
D: display books
S: stop the program
"""

user_choice = input(menu).strip().upper()[0]

book_store = []

while user_choice != 'S':
    if user_choice == 'A':
        book_store.append(add_book())
    elif user_choice == 'D':
        show_books(book_store)
    else:
        print(f"{user_choice} is not a valid option !!!\n")

    print()

    user_choice = input(menu).strip().upper()
