"""A program that can store and display books from a user's reading list
mini-project from Teclado"""

import os
import json


def add_book():  # Take information about books and puts them in books.json file
    books = load_books()

    book_title = input("Book title :    ").strip().title()
    author_name = input("Author's name: ").strip().title()
    year_of_publication = int(input("Publication's year:    ").strip())

    books.append({
        'Title': book_title,
        'Author': author_name,
        'Year': year_of_publication,
        'Status': "Unread"
    })

    with open('books.json', 'w') as books_store:
        json.dump(books, books_store)

    print("\n... your book is added\n")


def load_books():  # load all books.json file in our code

    with open('books.json') as books_store:
        return json.load(books_store)


def find_books():  # find a book by the title put by the user
    books = load_books()
    matching_books = []

    title = input("Please enter a book title to search: ").strip().title()

    for book in books:
        if title in book['Title']:
            matching_books.append(book)

    return matching_books


def delete_book(matching_books, books):  # delete the book which title match the title entered by the user
    books.remove(matching_books)


def mark_book(matching_books, books):  # mark as read the book which title match the title entered by the user
    index = books.index(matching_books)
    books[index]['Status'] = 'read'


def update_books_store(operation):  # Update the file book.json after modification by the user
    matching_books = find_books()
    books = load_books()

    if matching_books:
        operation(matching_books[0], books)

        with open('books.json', mode='w') as books_store:
            json.dump(books, books_store)
    else:
        print("Sorry, we didn't find any books for that search term.")


def show_books(books):  # Show the books
    print()

    for book in books:
        print(f"{book['Title']}, by {book['Author']} ({book['Year']}) - {book['Status']}")

    print()


menu = ("Please choose an operation\n"
        "A: add a book\n"
        "S: show all the books\n"
        "F: find a specific book\n"
        "M: mark a book as read\n"
        "D: delete a book\n"
        "E: end the program\n")

user_choice = input(menu).strip().upper()[0]

if os.path.isfile('./books.json') is False:  # Create a books.json file if it doesn't exist
    with open('./books.json', 'x') as books_store:
        json.dump([], books_store)

while user_choice != 'E':
    if user_choice == 'A':
        add_book()
    elif user_choice == 'S':
        reading_list = load_books()

        if reading_list:  # True si reading_list is not empty
            show_books(reading_list)
        else:
            print("Your reading list is empty!")

    elif user_choice == 'F':
        matching_list = find_books()

        if matching_list:  # True si reading_list is not empty
            show_books(matching_list)
        else:
            print("Sorry, we didn't find any books for that search term.")
    elif user_choice == 'M':
        update_books_store(mark_book)
    elif user_choice == 'D':
        update_books_store(delete_book)
    else:
        print(f"{user_choice} is not a valid option !!!\n")

    user_choice = input(menu).strip().upper()[0]
