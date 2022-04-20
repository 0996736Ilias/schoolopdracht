import json
import Book

bookJSON = "BookDatabase.json"


def readFromBookJSON():
    pass
    bookList = []

    with open(bookJSON, "r") as read_file:
        data = json.load(read_file)

    for row in data:
        bookList.append(
            Book.Book(row["author"], row["country"], row["imageLink"], row["language"], row["link"], row["pages"],
                      row["title"], row["ISBN"], row["year"]))

    return bookList


def readFromJSONReturnJSON():
    with open(bookJSON, "r") as read_file:
        data = json.load(read_file)

    return data


def deleteBook(ISBN):
    new_list = []
    with open(bookJSON, mode='r', newline='') as read_file:
        tmp = json.load(read_file)
        for r in tmp:
            if ISBN == r["ISBN"]:
                print("skip")
            else:
                new_list.append(r)
            print(r.__repr__())
    print(new_list)
    with open(bookJSON, mode='w', newline='') as read_file:
        json.dump(new_list, read_file, indent=4)
