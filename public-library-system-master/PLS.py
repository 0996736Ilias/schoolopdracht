import Person
import Librarian
import Subscriber
import Backup
import Book
import BookItem
import LoanItem
import Catalog

CURRENTUSER = 0


def setup():
    global userList, bookList, subscriberList, bookItemList
    userList = Person.readFromPersonCSV()
    bookList = Book.readFromBookJSON()
    subscriberList = Subscriber.readFromSubscriberCSV()
    bookItemList = BookItem.readFromBookItemCSV()


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


def userlist():
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







def editUser(id):
    global userList

    Person.editPerson(id)
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

    book = Book.Book(author, country, imageLink, language, link, pages, title, ISBN, year)
    bookItem = BookItem.BookItem(title, author, copies, ISBN)
    book.writeToDatabase(book)
    bookItem.writeToDatabase()


def borrowed():
    global CURRENTUSER
    LoanItem.loanedToPerson(CURRENTUSER)


def deleteBookItem():
    a = input("give ISBN of book please")
    deleteBookItem(a)


def editBookItem(ID):
    BookItem.editBookItem(ID)


def deleteBook():
    Book.deleteBook("9781234534597")


def login():
    username = input("[Login] Please login with your username: ")
    password = input("please use your password: ")
    checkUsername(username, password)


def mainMenu():
    global CURRENTUSER
    while True:
        if Librarian.librarianCheck(CURRENTUSER):
            print("[Menu] 1. Search book")
            print("[Menu] 2. Search book item")
            print("[Menu] 3. Add book")
            print("[Menu] 4. book list")
            print("[Menu] 5. Add bookItem")
            print("[Menu] 6. user list")
            print("[Menu] 7. Delete a user")
            print("[Menu] 8. Register new user")
            print("[Menu] 9. Logout")
            print("[Menu] 10. Make backup")
            print("[Menu] 11. Restore backup")
            print("[Menu] 12. Edit user")
            print("[Menu] 13. Edit book")
            print("[Menu] 14. Edit book item")
            print("[Menu] 15. Delete book item")
            print("[Menu] 16. Delete book ")

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


        elif option == "2"and Librarian.librarianCheck(CURRENTUSER):
            print("2")

        elif option == "3" and Librarian.librarianCheck(CURRENTUSER):
            addBook()

        elif option == "4" and Librarian.librarianCheck(CURRENTUSER):
            Book.bookList()

        elif option == "5" and Librarian.librarianCheck(CURRENTUSER):
            BookItem.

        elif option == "6" and Librarian.librarianCheck(CURRENTUSER):
            userlist()

        elif option == "7" and Librarian.librarianCheck(CURRENTUSER):
            Person.deletePerson(input("give user number to delete"))
        elif option == "8" and Librarian.librarianCheck(CURRENTUSER):
            register()
        elif option == "9" and Librarian.librarianCheck(CURRENTUSER):
            setup()
            CURRENTUSER = 0
            login()
        elif option == "10" and Librarian.librarianCheck(CURRENTUSER):
            Backup.backupMake()
        elif option == "11" and Librarian.librarianCheck(CURRENTUSER):
            Backup.backupRestoreMenu()
        elif option == "12" and Librarian.librarianCheck(CURRENTUSER):
            Person.editPerson(input("give the number of use you want to edit: "))
        elif option == "13" and Librarian.librarianCheck(CURRENTUSER):
            Book.editBook(input("give the ISBN of Book you want to edit: "))
        elif option == "14" and Librarian.librarianCheck(CURRENTUSER):
            BookItem.editBookItem(input("give the ISBN of book item you want to edit: "))
        elif option == "15" and Librarian.librarianCheck(CURRENTUSER):
            BookItem.deleteBookItem(input("give the ISBN of book item you want to delete: "))

        elif option == "3" and Librarian.librarianCheck(CURRENTUSER):
            LoanItem.returnItem(input("give ISBN of book you want to return"))
        elif option == "4" and Subscriber.SubscriberCheck(CURRENTUSER):
            Book.bookList()

        elif option == "5" and Subscriber.SubscriberCheck(CURRENTUSER):
            awnser = input("are you sure you want to delete this user [y/n]")
            if awnser == "y":
                Person.deletePerson(CURRENTUSER)
                print("user deleted")
                setup()
                CURRENTUSER = 0
                login()
            elif awnser == "n":
                mainMenu()
            else:
                print("invalid argument")
        elif option == "6" and Subscriber.SubscriberCheck(CURRENTUSER):
            userlist()

        else:
            print("[Menu] Invalid input. Please try again.")


setup()
login()
mainMenu()
