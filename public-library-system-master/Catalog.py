
import Book
import BookJSON
import json

class Catalog():
    """This is a catalog class"""
    def __init__(self):
        self.foundBooks = []
        self.bookList = BookJSON.readFromBookJSON()

    def chooseLoanBook(self):
        print("[Catalog]")
        iteration = 1
        for book in self.foundBooks:
            print("[Catalog] " + str(iteration) + " - " + book.title)
            iteration += 1

        if len(self.foundBooks) <= 0:
            print("[Catalog] No results found.")

        else:
            loopCheck = True
            while loopCheck:
                try:
                    chosenBook = int(input("[Catalog] Please input book number: "))
                except ValueError:
                    print("[Catalog] Invalid number, please try again.]")
                else:
                    for number in range(1, (len(self.foundBooks)+1)):
                        if chosenBook == number:
                            loopCheck = False
                    print("[Catalog] Invalid number, please try again.")

            print("[Catalog]")
            self.foundBooks[chosenBook-1].showBook()

    def searchBook(self):
        inCatalog = True
        bookList = BookJSON.readFromBookJSON()      
        searchKeywords = []
        searchInputArray = ""
        validInput = False
        print("[Catalog] Please type in your search criteria (title, author, country).")
        print("[Catalog] You can type in more than one or type 'none' for no criteria.")
        searchInput = input("[Catalog] >>> ")

        if "none" in searchInput.lower():
            self.chooseLoanBook()
            iteration = 1
            for book in bookList:
                print("[Catalog] " + str(iteration) + " - " + book.title)
                iteration += 1
                

            loopCheck = True
            while loopCheck:
                try:
                    chosenBook = int(input("[Catalog] Please input book number: "))
                except ValueError:
                    print("[Catalog] Invalid number, please try again.")
                else:
                    for number in range(1, (len(self.bookList)+1)):
                        if chosenBook == number:
                            loopCheck = False
                    if loopCheck:
                        print("[Catalog] Invalid number, please try again.")   
                         
            print("[Catalog]")
            self.bookList[chosenBook-1].showBook()
            inCatalog = False

        if "title" in searchInput.lower():
                searchInputArray += "title"
                searchKeywords.append(input("[Catalog] Fill in the title >>> "))   
                validInput = True 

        if "author" in searchInput.lower():
                searchInputArray += "author"
                searchKeywords.append(input("[Catalog] Fill in the author >>> "))
                validInput = True

        if "country" in searchInput.lower():
                searchInputArray += "country"
                searchKeywords.append(input("[Catalog] Fill in the country >>> "))    
                validInput = True

        if not validInput and inCatalog:
            print("[Catalog]\n[Catalog] Invalid input, please try again.\n[Catalog]")
            self.searchBook()

        for criteria in searchKeywords:
                for book in bookList:
                    if criteria.lower() in book.title.lower() and "title" in searchInputArray:
                        self.foundBooks.append(book)
                    if criteria.lower() in book.author.lower() and "author" in searchInputArray:
                        self.foundBooks.append(book)
                    if criteria.lower() in book.country.lower() and "country" in searchInputArray:
                        self.foundBooks.append(book)

        if inCatalog:
            self.chooseLoanBook()

            
