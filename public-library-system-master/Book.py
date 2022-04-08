import json
import BookItemCSV
import LoanItem
import PersonCSV

CURRENTUSER = 0

class Book():  
    """This is a book class"""
    def __init__(self, author, country, imageLink, language, link, pages, 
    title, year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.title = title
        self.year = year

    def writeToDatabase(self, book):
        with open('BookDatabase.json') as json_file:
            data  = json.load(json_file)
            
            book_data = {
                "author": self.author,
                "country": self.country,
                "imageLink": self.imageLink,
                "language": self.language,
                "link": self.link,
                "pages": self.pages,
                "title": self.title,
                "year": self.year
            }
            data.append(book_data)

            self.writeToJson(data)
    
    def writeToJson(self, data):
        with open("BookDatabase.json", 'w',) as f:
            json.dump(data, f, indent=4)
        
    
    def showBook(self):
        print("[Book] Author: " + self.author)
        print("[Book] Country: " + self.country)
        print("[Book] Image Link: " + self.imageLink)
        print("[Book] Language: " + self.language)
        print("[Book] Link: " + self.link)
        print("[Book] Pages: " + str(self.pages))
        print("[Book] Title: " + self.title)
        print("[Book] Year: " + str(self.year))
        
        if LoanItem.loanAvailabilityCheck(self.findISBN(), self.author, self.title):
            while True:
                print("[Book]")
                userInput = input("[Book] Would you like loan this book (y/n): ")
                if userInput == "y":
                    loanItem = LoanItem.LoanItem(CURRENTUSER, 14, self.findISBN())
                    loanItem.writeToDatabase()
                    print("[Book] Loan successfully administrated.")   
                    print("[Book]")                
                    break
                if userInput == "n":
                    break
                print("[Book] Invalid input, please try again. ")
        else:
            input("[Book] No book available, press any key to go back!")

    def findISBN(self):
        bookItemList = BookItemCSV.readFromBookItemCSV()
        for bookItem in bookItemList:
            if bookItem.author == self.author and bookItem.title == self.title:
                return bookItem.ISBN

def setCurrentUses(usernumber):
    global CURRENTUSER
    CURRENTUSER = usernumber