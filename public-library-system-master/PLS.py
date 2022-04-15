import BookItemCSV
import Person
import PersonCSV
import BookJSON
import Librarian
import Subscriber
import Backup
import Book
import BookItem
from sys import exit

import Catalog

CURRENTUSER = 0


def setup():
    global userList, bookList, subscriberList, bookItemList
    userList = PersonCSV.readFromPersonCSV()
    bookList = BookJSON.readFromBookJSON()
    subscriberList = Subscriber.readFromSubscriberCSV()
    bookItemList = BookItemCSV.readFromBookItemCSV()


def checkUsername(username, password):
    global userList, CURRENTUSER

    for user in userList:

        a = getattr(user, "username")
        b = getattr(user, "password")
        if username == "admin" and password == "admin":
            CURRENTUSER = user.number
            Book.setCurrentUses(CURRENTUSER)
        if username == a and password == b:
            CURRENTUSER = user.number
            Book.setCurrentUses(CURRENTUSER)

    if CURRENTUSER == 0:
        print("[Login] wrong username or password, please try again!")
        login()


def userlist():  # try to get from persons to subscribers Reech1950
    global subscriberList, userList
    for j in userList:
        a = getattr(j, "username")
        for Number in subscriberList:
            b = getattr(j, "number")
            if Number == b:
                print(a)


def printBookItems():
    global bookItemList
    for j in bookItemList:
        print(j)


def printBooks():
    global bookList
    for j in bookList:
        print(j)


def deleteUser(id):
    global userList, CURRENTUSER

    PersonCSV.deletePerson(id)
    print("user deleted")
    setup()
    CURRENTUSER = 0
    login()


def editUser(id):
    global userList

    PersonCSV.editPerson(id)
    print("user Edited")


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
        personType = input("[Register] Is this person a Librarian or Subscriber (librarian/subscriber): ")
        if personType == "librarian" or personType == "subscriber":
            break
        print("[Register] Invalid input, please try again!")

    person = Person.Person(number, givenName, surname,
                           streetAddress, zipCode, city, emailAddress, userName.lower(), password, telephoneNumber)
    person.writeToDatabase(personType)
    print("[Register]\n[Register] Register Successful\n[Register]")
    setup()


def addBook():
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

    book = Book.Book(author, country, imageLink, language, link, pages,
                     title, ISBN, year)
    bookItem = BookItem.BookItem(title, author, copies, ISBN)
    book.writeToDatabase(book)
    bookItem.writeToDatabase()


def borrowed():
    borrowed =

def deleteBookItem():
    a = input("give ISBN of book please")
    BookItemCSV.deleteBookItem(a)


def editBookItem(ID):
    BookItemCSV.editBookItem(ID)


def login():
    username = input("[Login] Please login with your username: ")
    password = input("please use your password: ")
    checkUsername(username, password)


def mainMenu():
    global CURRENTUSER
    while True:
        if Librarian.librarianCheck(CURRENTUSER):
            print("[Menu] 1. Search book")
            print("[Menu] 3. Search book item")
            print("[Menu] 3. Add book")
            print("[Menu] 3. book list")
            print("[Menu] 3. Add bookItem")
            print("[Menu] 3. user list")
            print("[Menu] 3. Delete a user")
            print("[Menu] 4. Register new user")
            print("[Menu] 2. Logout")

            print("[Menu] 4. Make backup")
            print("[Menu] 5. Restore backup")
            print("[Menu] 6. Delete a user")

        elif Subscriber.SubscriberCheck(CURRENTUSER):
            print("[Menu] 1. Search book")

            print("[Menu] 2. Logout")
            print("[Menu] 3. Delete user user")
            print("[Menu] 4. return book")
            print("[Menu] 5. Edit current user")

        option = input("[Menu]\n[Menu] Choice: ")
        if option == "1":
            catalog = Catalog.Catalog()
            catalog.searchBook()

        elif option == "2":
            setup()
            CURRENTUSER = 0
            login()

        elif option == "3" and Librarian.librarianCheck(CURRENTUSER):
            addBook()

        elif option == "4" and Librarian.librarianCheck(CURRENTUSER):
            Backup.backupMake()

        elif option == "5" and Librarian.librarianCheck(CURRENTUSER):
            Backup.backupRestoreMenu()

        elif option == "6" and Librarian.librarianCheck(CURRENTUSER):
            register()
        else:
            print("[Menu] Invalid input. Please try again.")


setup()
login()
mainMenu()
