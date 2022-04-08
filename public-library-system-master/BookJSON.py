import json
import Book

def readFromBookJSON():
    pass
    bookList = []

    with open ("BookDatabase.json", "r") as read_file:
        data = json.load(read_file)
    
    for row in data:    
        bookList.append( Book.Book(row["author"], row["country"], row["imageLink"], row["language"], row["link"], row["pages"], row["title"], row["year"]) )
    
    return bookList

def readFromJSONReturnJSON():
    with open ("BookDatabase.json", "r") as read_file:
        data = json.load(read_file)
    
    return data