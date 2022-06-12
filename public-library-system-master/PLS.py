import Person
import Admin
import Member
import DataManagement
import Book
import BookItem
import LoanItem
import Catalog
import csv
import json


class PLS():
    def __init__(self):
        self.CURRENTUSER = 0
        self.userList = self.readFromPersonCSV()
        # self.bookList = self.readFromBookJSON()
        self.subscriberList = self.readFromMemberrCSV()
        self.bookItemList = self.readFromBookItemCSV()
        self.librarianList = self.readFromAdminCSV()

    def readFromBookJSON(self):
        bookList = []

        with open("BookDatabase.json", "r") as read_file:
            data = json.load(read_file)

        for row in data:
            bookList.append(
                Book.Book(row["author"], row["country"], row["imageLink"], row["language"], row["link"], row["pages"],
                          row["title"], row["ISBN"], row["year"]))

        return bookList

    def readFromBookItemCSV(self):
        bookItemList = []

        with open("BookItemDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for r in csv_reader:
                bookItemList.append(BookItem.BookItem(r[0], r[1], r[2], r[3]))

        return bookItemList

    def readFromLoanItemCSV(self):
        loanItemList = []

        with open("loanAdministrationDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for r in csv_reader:
                loanItemList.append(LoanItem.LoanItem(r[0], r[1], r[2]))
        return loanItemList

    def loandBooks(self):
        with open("loanAdministrationDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for r in csv_reader:
                with open("BookItemDatabase.csv", mode='r') as books:
                    bookItems = csv.reader(books, delimiter=',')
                    for i in bookItems:
                        if (r[2] == i[3]):
                            if (i[3] != 'ISBN'):
                                print(str(i) + ' by user with ID ' + r[0])
                            else:
                                print(i)

    def readFromPersonCSV(self):
        with open("PersonDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            List = []
            for r in csv_reader:
                List.append(Person.Person(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]))
        return List

    def readFromMemberrCSV(self):
        numberList = []

        with open("MemberDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for r in csv_reader:
                numberList.append((r[0]))

        return numberList

    def readFromAdminCSV(self):
        numberList = []

        with open("AdminDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for r in csv_reader:
                numberList.append((r[0]))

        return numberList

    def checkUsername(self, username, password):
        for user in self.userList:

            a = getattr(user, "username")
            b = getattr(user, "password")

            if username == a and password == b:
                self.CURRENTUSER = user.number
                return

        if username == "admin" and password == "admin123":
            person = Admin.Admin(int(self.userList[-1].number) + 1, "admin", "admin",
                                 "admin", "admin", "admin", "admin", "admin".lower(), "admin123",
                                 "admin")
            person.writeToDatabase()
            self.CURRENTUSER = person.number
            print("Pleas restart program")
            return

        if self.CURRENTUSER == 0:
            print("[Login] wrong username or password, please try again!")
            self.login()

    def AdminCheck(self, number):
        if number in self.librarianList:
            return True

    def MemberCheck(self, number):
        numberList = self.readFromMemberrCSV()
        if number in numberList:
            return True

    def register(self):
        number = int(self.userList[-1].number) + 1
        print("[Register] Register a person by filling in the information.")
        while True:
            givenName = input("[Register] GivenName: ")
            surname = input("[Register] Surname: ")
            streetAddress = input("[Register] Street Address: ")
            zipCode = input("[Register] Zip Code: ")
            city = input("[Register] City: ")
            emailAddress = input("[Register] Email Address: ")
            userName = input("[Register] Username: ")
            password = input("[Register] Password: ")
            telephoneNumber = input("[Register] Telephone Number: ")
            if givenName != "" and surname != "" and streetAddress != "" and zipCode != "" and city != "" and emailAddress != "" and userName != "" and password != "" and telephoneNumber != "" :
                break
            print("[Register] Invalid input, please try again!")
        while True:
            personType = input("[Register] Is this person a Admin or Member (admin/member): ")
            if personType == "admin" or personType == "member":
                break
            print("[Register] Invalid input, please try again!")
        if personType == "admin":
            person = Admin.Admin(number, givenName, surname,
                                 streetAddress, zipCode, city, emailAddress, userName.lower(), password,
                                 telephoneNumber)
        if personType == "member":
            person = Member.Member(number, givenName, surname,
                                   streetAddress, zipCode, city, emailAddress, userName.lower(), password,
                                   telephoneNumber)
        person.writeToDatabase()
        print("[Register]\n[Register] Register Successful\n[Register]")
        self.__init__()
    def login(self):
        username = input("[Login] Please login with your username: ")
        password = input("please use your password: ")
        self.checkUsername(username, password)

    def mainMenu(self):
        while True:
            if self.AdminCheck(self.CURRENTUSER):
                print("\n[        BOOKS       ]")
                print("[Menu] 1.  Search book")
                print("[Menu] 2.  book list")
                print("[Menu] 3.  see loaned books")
                print("[Menu] 4.  return book ")
                print("[Menu] 5.  Add book")
                print("[Menu] 6.  Edit book")
                print("[Menu] 7.  Delete book ")
                print("\n[     BOOKITEMS       ]")
                print("[Menu] 8.  Search book item")
                print("[Menu] 9.  Book item list ")
                print("[Menu] 10. Delete book item")
                print("[Menu] 11. Edit book item")
                print("\n[     USER MANAGEMENT     ]")
                print("[Menu] 12. user list")
                print("[Menu] 13. Register new user")
                print("[Menu] 14. Edit user")
                print("[Menu] 15. Delete a user")
                print("\n[     DATA MANAGEMENT     ]")
                print("[Menu] 16. Make backup")
                print("[Menu] 17. Restore backup")
                print("[Menu] 18. Add list of users")
                print("[Menu] 19. Add list of books")
                print("[Menu] 20. Load in users")
                print("[Menu] 21. load in books")
                print("\n[     OTHER       ]")
                print("[Menu] 22. Logout")
                print("[Menu] 23. exit ")
            elif self.MemberCheck(self.CURRENTUSER):
                print("[Menu] 1.  Search book")
                print("[Menu] 2.  Book list")
                print("[Menu] 3.  return book")
                print("[Menu] 4.  Logout")
                print("[Menu] 5.  exit ")

            option = input("\n[Menu] Choice: ")
            if option == "1":
                catalog = Catalog.Catalog()
                catalog.searchBook(self.CURRENTUSER)
            elif option == "2":

                a = Admin.Admin("none", "none", "none", "none", "none",
                                "none", "none", "none", "none", "none")
                a.printBooks()
            elif option == "3" and self.AdminCheck(self.CURRENTUSER):
                self.loandBooks()
            elif option == "4" and self.AdminCheck(self.CURRENTUSER):
                a = LoanItem.LoanItem("none", "none", input("give ISBN of book you want to return"))
                a.returnItem(input("give number of user from who the book is"))
            elif option == "5" and self.AdminCheck(self.CURRENTUSER):
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

            elif option == "6" and self.AdminCheck(self.CURRENTUSER):
                a = Book.Book("none", "none", "none", "none", "none", "none", "none",
                              input("give the ISBN of book you want to edit: "), "none")
                a.editBook()
            elif option == "7" and self.AdminCheck(self.CURRENTUSER):
                a = Book.Book("none", "none", "none", "none", "none", "none", "none",
                              input("give the ISBN of book you want to delete: "), "none")
                a.deleteBook()


            elif option == "8" and self.AdminCheck(self.CURRENTUSER):
                a = Admin.Admin("none", "none", "none", "none", "none",
                                "none", "none", "none", "none", "none")
                a.bookItemSearch()

            elif option == "9" and self.AdminCheck(self.CURRENTUSER):
                a = Admin.Admin("none", "none", "none", "none", "none",
                                "none", "none", "none", "none", "none")
                a.printBookItems()
            elif option == "10" and self.AdminCheck(self.CURRENTUSER):
                a = BookItem.BookItem("none", "none", "none", input("give the ISBN of bookitem you want to delete: "))
                a.deleteBookItem()
            elif option == "11" and self.AdminCheck(self.CURRENTUSER):
                a = BookItem.BookItem("none", "none", "none", input("give the ISBN of bookitem you want to edit: "))
                a.editBookItem()
            elif option == "12" and self.AdminCheck(self.CURRENTUSER):
                a = Admin.Admin("none", "none", "none", "none", "none",
                                "none", "none", "none", "none", "none")
                a.userlist()
            elif option == "13" and self.AdminCheck(self.CURRENTUSER):
                self.register()
            elif option == "14" and self.AdminCheck(self.CURRENTUSER):
                a = Person.Person(input("give the number of use you want to edit: "), "none", "none", "none", "none",
                                  "none", "none", "none", "none", "none")
                a.editPerson()
            elif option == "15" and self.AdminCheck(self.CURRENTUSER):
                c = input("give the number of user you want to use: ")

                if self.AdminCheck(c):
                    a = Admin.Admin(c, "none", "none", "none", "none",
                                    "none", "none", "none", "none", "none")
                else:
                    a = Member.Member(c, "none", "none", "none", "none",
                                      "none", "none", "none", "none", "test")
                a.delete()
            elif option == "16" and self.AdminCheck(self.CURRENTUSER):
                DataManagement.DataManagement.backupMake()

            elif option == "17" and self.AdminCheck(self.CURRENTUSER):
                DataManagement.DataManagement.backupRestoreMenu()
            elif option == "18" and self.AdminCheck(self.CURRENTUSER):
                DataManagement.DataManagement.addListOfUsers()

            elif option == "19" and self.AdminCheck(self.CURRENTUSER):
                DataManagement.DataManagement.addListOfBooks()
            elif option == "20" and self.AdminCheck(self.CURRENTUSER):
                DataManagement.DataManagement.loadInUsers()

            elif option == "21" and self.AdminCheck(self.CURRENTUSER):
                DataManagement.DataManagement.loadInBookJSON()
            elif option == "22" and self.AdminCheck(self.CURRENTUSER):
                self.__init__()
                self.login()

            elif option == "23" and self.AdminCheck(self.CURRENTUSER):
                exit()

            elif option == "3" and self.MemberCheck(self.CURRENTUSER):
                print(self.readFromBookJSON())

            elif option == "4" and self.MemberCheck(self.CURRENTUSER):
                a = LoanItem.LoanItem("none", "none", input("give ISBN of book you want to return"))
                a.returnItem(self.CURRENTUSER)
            elif option == "2" and self.MemberCheck(self.CURRENTUSER):
                self.__init__()
                self.login()
            elif option == "5" and self.MemberCheck(self.CURRENTUSER):
                exit()
            else:
                print("[Menu] Invalid input. Please try again.")

    def startup(self):
        self.login()
        self.mainMenu()


a = PLS()
a.startup()
