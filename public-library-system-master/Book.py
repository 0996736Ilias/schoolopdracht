import json
import BookItem
import LoanItem
import csv
CURRENTUSER = 0


class Book():
    """This is a book class"""

    def __init__(self, author, country, imageLink, language, link, pages, title, isbn,
                 year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.ISBN = isbn
        self.title = title
        self.year = year

    def __repr__(self):
        return self.author + ", " + self.country + ", " + self.imageLink + ", " + self.language + ", " + str(
            self.link) + ", " + str(self.pages) + ", " + self.title + ", " + str(self.ISBN) + ", " + str(self.year) + "\n"

    def writeToDatabase(self):
        with open('BookDatabase.json') as json_file:
            data = json.load(json_file)

            book_data = {
                "author": self.author,
                "country": self.country,
                "imageLink": self.imageLink,
                "language": self.language,
                "link": self.link,
                "pages": self.pages,
                "title": self.title,
                "ISBN": self.ISBN,
                "year": self.year
            }
            data.append(book_data)
        with open("BookDatabase.json", 'w', ) as f:
            json.dump(data, f, indent=4)

    def showBook(self, CURRENTUSER):
        print("[Book] Author: " + self.author)
        print("[Book] Country: " + self.country)
        print("[Book] Image Link: " + self.imageLink)
        print("[Book] Language: " + self.language)
        print("[Book] Link: " + self.link)
        print("[Book] ISBN: " + str(self.ISBN))
        print("[Book] Pages: " + str(self.pages))
        print("[Book] Title: " + self.title)
        print("[Book] Year: " + str(self.year))
        a = LoanItem.LoanItem("none", "none", "none")
        if a.loanAvailabilityCheck(self.findISBN(), self.author, self.title):
            while True:
                print("[Book]")
                userInput = input("[Book] Would you like loan this book (y/n): ")
                if userInput == "y":
                    if LoanItem.LoanItem.limitCheck(CURRENTUSER) == False:
                        print("user already has 3 books")
                        break
                    loanItem = LoanItem.LoanItem(CURRENTUSER, 30, self.findISBN())
                    loanItem.writeToDatabase()
                    print("[Book] Loan successfully administrated.")
                    print("[Book]")
                    break
                if userInput == "n":
                    return
                print("[Book] Invalid input, please try again. ")
        else:
            input("[Book] No book available, press any key to go back!")

    def findISBN(self):

        bookItemList = []

        with open("BookItemDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for r in csv_reader:
                bookItemList.append(BookItem.BookItem(r[0], r[1], r[2], r[3]))
        for bookItem in bookItemList:
            if bookItem.author == self.author and bookItem.title == self.title:
                return bookItem.ISBN

    def deleteBook(self):
        new_list = []
        with open("BookDatabase.json", mode='r', newline='') as read_file:
            tmp = json.load(read_file)
            for r in tmp:
                if self.ISBN == r['ISBN']:
                    print("skip")
                else:
                    new_list.append(r)
                print(r.__repr__())
        print(new_list)
        with open("BookDatabase.json", mode='w', newline='') as read_file:
            json.dump(new_list, read_file, indent=4)

    def editBook(self):
        new_list = []
        with open("BookDatabase.json", mode='r', newline='') as read_file:
            tmp = json.load(read_file)
            for r in tmp:
                if r['ISBN'] == self.ISBN:
                    r["author"] = input("new author ")
                    r["country"] = input("new country ")
                    r["imageLink"] = input("new imageLink ")
                    r["language"] = input("new language")
                    r["link"] = input("new link")
                    r["pages"] = input("new pages")
                    r["title"] = input("new title")
                    r["year"] = input("new year")
                    new_list.append(r)
                else:
                    new_list.append(r)

        with open("BookDatabase.json", mode='w', newline='') as read_file:
            json.dump(new_list, read_file, indent=4)
