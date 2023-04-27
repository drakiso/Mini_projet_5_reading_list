"""A program that can store and display books from a user's reading list
mini-project from Teclado"""

import csv
import os


def add_book():  # Take information about books / verify if books.csv, create it if not
    # put books information in the file
    book_title = input("Book title :    ").strip().title()
    author_name = input("Author's name: ").strip().title()
    year_of_publication = int(input("Publication's year:    ").strip())
    status = "Unread"

    fieldnames = ['Title', 'Author', 'Year', 'Status']

    if os.path.isfile('./books.csv'):
        with open('books.csv', 'a') as books_store:
            writer = csv.DictWriter(books_store, delimiter=',', fieldnames=fieldnames)
            writer.writerow(dict(Title=book_title, Author=author_name, Year=year_of_publication, Status=status))
    else:
        with open('books.csv', 'w') as books_store:
            writer = csv.DictWriter(books_store, delimiter=',', fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(dict(Title=book_title, Author=author_name, Year=year_of_publication, Status=status))

    print("\n... your book is added\n")


def load_books():  # load all books.csv file in our code
    books = []

    with open('books.csv') as books_store:
        reader = csv.DictReader(books_store, delimiter=',', skipinitialspace=True)

        for row in reader:
            books.append(row)

    return books


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


def update_books_store(operation):  # Update the file book.csv after modification by the user
    matching_books = find_books()
    books = load_books()

    if matching_books:
        operation(matching_books[0], books)

        with open('books.csv', mode='w') as books_store:
            writer = csv.DictWriter(books_store, delimiter=',', fieldnames=['Title', 'Author', 'Year', 'Status'])

            writer.writeheader()

            for book in books:
                writer.writerow(
                    {'Title': book['Title'], 'Author': book['Author'], 'Year': book['Year'], 'Status': book['Status']})
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
