import Person
import Admin
import Member
import Backup
import Book
import BookItem
import LoanItem
import Catalog
import csv
import json

CURRENTUSER = 0


def setup():
    global userList, bookList, subscriberList, bookItemList, librarianList
    userList = readFromPersonCSV()
    bookList = readFromBookJSON()
    subscriberList = readFromMemberrCSV()
    bookItemList = readFromBookItemCSV()
    librarianList = readFromAdminCSV()


def readFromBookJSON():
    bookList = []

    with open("BookDatabase.json", "r") as read_file:
        data = json.load(read_file)

    for row in data:
        bookList.append(
            Book.Book(row["author"], row["country"], row["imageLink"], row["language"], row["link"], row["pages"],
                      row["title"], row["ISBN"], row["year"]))

    return bookList


def readFromBookItemCSV():
    bookItemList = []

    with open("BookItemDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for r in csv_reader:
            bookItemList.append(BookItem.BookItem(r[0], r[1], r[2], r[3]))

    return bookItemList


def readFromLoanItemCSV():
    loanItemList = []

    with open("loanAdministrationDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for r in csv_reader:
            loanItemList.append(LoanItem.LoanItem(r[0], r[1], r[2]))
    return loanItemList
def loandBooks():
    with open("loanAdministrationDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for r in csv_reader:
            with open("BookItemDatabase.csv", mode='r') as books:
                bookItems = csv.reader(books, delimiter=',')
                for i in  bookItems:
                    if(r[2] == i[3] ):
                        if (i[3] != 'ISBN'):
                            print(str(i) + ' by user with ID ' + r[0])
                        else:
                            print(i)



def readFromPersonCSV():
    with open("PersonDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        List = []
        for r in csv_reader:
            List.append(Person.Person(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]))
    return List


def readFromMemberrCSV():
    numberList = []

    with open("MemberDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for r in csv_reader:
            numberList.append((r[0]))

    return numberList

def readFromAdminCSV():
    numberList = []

    with open("AdminDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for r in csv_reader:
            numberList.append((r[0]))

    return numberList

def checkUsername(username, password):
    global userList, CURRENTUSER

    for user in userList:

        a = getattr(user, "username")
        b = getattr(user, "password")

        if username == a and password == b:
            CURRENTUSER = user.number
            return

    if username == "admin" and password == "admin123":
        person = Admin.Admin(int(userList[-1].number) + 1, "admin", "admin",
                                     "admin", "admin", "admin", "admin", "admin".lower(), "admin123",
                                     "admin")
        person.writeToDatabase()
        CURRENTUSER = person.number
        print("Pleas restart program")
        return

    if CURRENTUSER == 0:
        print("[Login] wrong username or password, please try again!")
        login()

def AdminCheck(number):
    global librarianList
    if number in librarianList:
        return True


def MemberCheck(number):
    numberList = readFromMemberrCSV()
    if number in numberList:
        return True


def register():
    number = int(userList[-1].number) + 1
    print("[Register] Register a person by filling in the information.")
    givenName = input("[Register] GivenName: ")
    surname = input("[Register] Surname: ")
    streetAddress = input("[Register] Street Address: ")
    zipCode = input("[Register] Zip Code: ")
    city = input("[Register] City: ")
    emailAddress = input("[Register] Email Address: ")
    userName = input("[Register] Username: ")
    password = input("[Register] Password: ")
    telephoneNumber = input("[Register] Telephone Number: ")

    while True:
        personType = input("[Register] Is this person a Admin or Member (librarian/subscriber): ")
        if personType == "librarian" or personType == "subscriber":
            break
        print("[Register] Invalid input, please try again!")
    if personType == "librarian":
        person = Admin.Admin(number, givenName, surname,
                                 streetAddress, zipCode, city, emailAddress, userName.lower(), password,
                                 telephoneNumber)
    if personType == "subscriber":
        person = Member.Member(number, givenName, surname,
                                   streetAddress, zipCode, city, emailAddress, userName.lower(), password,
                                   telephoneNumber)
    person.writeToDatabase()
    print("[Register]\n[Register] Register Successful\n[Register]")
    setup()


def login():
    username = input("[Login] Please login with your username: ")
    password = input("please use your password: ")
    checkUsername(username, password)


def mainMenu():
    global CURRENTUSER
    while True:
        if AdminCheck(CURRENTUSER):
            print("\n[        BOOKS       ]")
            print("[Menu] 1. 1. Search book")
            print("[Menu] 4. 4. book list")
            print("[Menu] 16 16. return book ")
            print("[Menu] 3. 3. Add book")
            print("[Menu] 15 15. Delete book ")
            print("[Menu] 12 12. Edit book")
            print("\n[        BOOKITEMS       ]")
            print("[Menu] 2. 2. Search book item")
            print("[Menu] 17 17. book item list ")
            print("[Menu] 14 14. Delete book item")
            print("[Menu] 13 13. Edit book item")
            print("\n[        USER MANAGEMENT     ]")
            print("[Menu] 5. 5. user list")
            print("[Menu] 7. 7. Register new user")
            print("[Menu] 6. 6. Delete a user")
            print("[Menu] 11 11. Edit user")
            print("\n[        DATA MANAGEMENT     ]")
            print("[Menu] 9. 9. Make backup")
            print("[Menu] 10 10. Restore backup")
            print("\n[        OTHER       ]")
            print("[Menu] 8. 8. Logout")
            print("[Menu] 18 18. exit ")
        elif MemberCheck(CURRENTUSER):
            print("[Menu] 1. Search book")
            print("[Menu] 2. Logout")
            print("[Menu] 3. Book list")
            print("[Menu] 4. return book")
            print("[Menu] 5. exit ")

        option = input("[Menu]\n[Menu] Choice: ")
        if option == "1":
            catalog = Catalog.Catalog()
            catalog.searchBook(CURRENTUSER)


        elif option == "2" and AdminCheck(CURRENTUSER):
            a = Admin.Admin("none", "none", "none", "none", "none",
                            "none", "none", "none", "none", "none")
            a.bookItemSearch()
        elif option == "3" and AdminCheck(CURRENTUSER):
            print("[Book] Add a Book by filing in the information.")
            author = input("[Book] Author: ")
            country = input("[Book] Country: ")
            imageLink = input("[Book] ImageLink: ")
            language = input("[Book] Language: ")
            link = input("[Book] Link: ")

            while True:
                try:
                    pages = int(input("[Book] Pages: "))
                except ValueError:
                    print("[Book] Invalid number, please try again.")
                else:
                    break

            title = input("[Book] Title: ")

            while True:
                try:
                    year = int(input("[Book] Year: "))
                except ValueError:
                    print("[Book] Invalid number, please try again.")
                else:
                    break

            while True:
                try:
                    ISBN = int(input("[Book] ISBN: "))
                except ValueError:
                    print("[Book] Invalid number, please try again.")
                else:
                    break

            while True:
                try:
                    copies = int(input("[Book] Copies: "))
                except ValueError:
                    print("[Book] Invalid number, please try again.")
                else:
                    break

            book = Book.Book(author, country, imageLink, language, link, pages, title, ISBN, year)
            bookItem = BookItem.BookItem(title, author, copies, ISBN)
            book.writeToDatabase()
            bookItem.writeToDatabase()
        elif option == "4" and AdminCheck(CURRENTUSER):

            a = Admin.Admin("none", "none", "none", "none", "none",
                                    "none", "none", "none", "none", "none")
            a.printBooks()
        elif option == "5" and AdminCheck(CURRENTUSER):
            a = Admin.Admin("none", "none", "none", "none", "none",
                                    "none", "none", "none", "none", "none")
            a.userlist()
        elif option == "6" and AdminCheck(CURRENTUSER):
            c = input("give the number of user you want to use: ")

            if AdminCheck(c):
                a = Admin.Admin(c, "none", "none", "none", "none",
                                        "none", "none", "none", "none", "none")
            else:
                a = Member.Member(c, "none", "none", "none", "none",
                                          "none", "none", "none", "none", "none")
            a.delete()
        elif option == "7" and AdminCheck(CURRENTUSER):
            register()
        elif option == "8" and AdminCheck(CURRENTUSER):
            setup()
            CURRENTUSER = 0
            login()
        elif option == "9" and AdminCheck(CURRENTUSER):
            Backup.backupMake()
        elif option == "10" and AdminCheck(CURRENTUSER):
            Backup.backupRestoreMenu()
        elif option == "11" and AdminCheck(CURRENTUSER):
            a = Person.Person(input("give the number of use you want to edit: "), "none", "none", "none", "none",
                              "none", "none", "none", "none", "none")
            a.editPerson()

        elif option == "12" and AdminCheck(CURRENTUSER):
            a = Book.Book("none", "none", "none", "none", "none", "none", "none",
                          input("give the ISBN of book you want to edit: "), "none")
            a.editBook()
        elif option == "13" and AdminCheck(CURRENTUSER):
            a = BookItem.BookItem("none", "none", "none", input("give the ISBN of bookitem you want to edit: "))
            a.editBookItem()
        elif option == "14" and AdminCheck(CURRENTUSER):
            a = BookItem.BookItem("none", "none", "none", input("give the ISBN of bookitem you want to delete: "))
            a.deleteBookItem()
        elif option == "15" and AdminCheck(CURRENTUSER):
            a = Book.Book("none", "none", "none", "none", "none", "none", "none",
                          input("give the ISBN of book you want to delete: "), "none")
            a.deleteBook()
        elif option == "16" and AdminCheck(CURRENTUSER):
            a = LoanItem.LoanItem("none", "none", input("give ISBN of book you want to return"))
            a.returnItem(input("give number of user from who the book is"))
        elif option == "17" and AdminCheck(CURRENTUSER):
            a = Admin.Admin("none", "none", "none", "none", "none",
                                    "none", "none", "none", "none", "none")
            a.bookItemSearch()
        elif option == "18" and AdminCheck(CURRENTUSER):
            exit()
        elif option == "19" and AdminCheck(CURRENTUSER):
            loandBooks()
        elif option == "2" and MemberCheck(CURRENTUSER):
            setup()
            CURRENTUSER = 0
            login()
        elif option == "3" and MemberCheck(CURRENTUSER):
            print(readFromBookJSON())
        elif option == "4" and MemberCheck(CURRENTUSER):
            a = LoanItem.LoanItem("none", "none", input("give ISBN of book you want to return"))
            a.returnItem(CURRENTUSER)
        elif option == "5" and MemberCheck(CURRENTUSER):
            exit()
        else:
            print("[Menu] Invalid input. Please try again.")


setup()
login()
mainMenu()
