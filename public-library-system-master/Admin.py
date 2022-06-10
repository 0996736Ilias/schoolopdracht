import csv
import json
import Book
from Person import Person
from BookItem import BookItem


class Admin(Person):
    """This is a Admin class"""
    def userlist(self):
        with open("PersonDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            List = []
            for r in csv_reader:
                List.append(Person(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]))

        for j in List:
            print(j.__repr__())
    def editPerson(self):
        a = Person(input("give the number of use you want to edit: "), "none", "none", "none", "none",
                          "none", "none", "none", "none", "none")
        a.editPerson()

    def writeToDatabase(self):
        row_contents = [self.number, self.givenName, self.surname,
                        self.streetAddress, self.zipCode, self.city, self.emailAddress, self.username, self.password,
                        self.telephonenumber]

        with open("PersonDatabase.csv", 'a', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(row_contents)
        with open("AdminDatabase.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow([self.number])

    def delete(self):
        with open("PersonDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            List = []
            for r in csv_reader:
                List.append(Person(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]))

        with open("PersonDatabase.csv", mode='w', newline='') as csv_file:
            tmp = []
            writer = csv.writer(csv_file)
            for r in List:
                if str(self.number) == r.number:
                    print("[PersonCSV] SKIP")
                else:
                    tmp.append(r.__repr__())
            print(tmp)

            writer.writerows(tmp)

        numberlist = []

        with open("AdminDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for r in csv_reader:
                numberlist.append((r[0]))
        with open("AdminDatabase.csv", mode='w', newline='') as csv_file:
            tmp = []
            writer = csv.writer(csv_file)
            for r in numberlist:
                if self.number == str(r):
                    print("[Admin] SKIP")
                else:
                    tmp.append([r])
            print(tmp)
            writer.writerows(tmp)

    def printBooks(self):
        bookList = []

        with open("BookDatabase.json", "r") as read_file:
            data = json.load(read_file)

        for row in data:
            bookList.append(
                Book.Book(row["author"], row["country"], row["imageLink"], row["language"], row["link"], row["pages"],
                          row["title"], row["ISBN"], row["year"]))
        for j in bookList:
            print(j)

    def printBookItems(self):
        bookItemList = []

        with open("BookItemDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for r in csv_reader:
                bookItemList.append(BookItem(r[0], r[1], r[2], r[3]))
                print(r)

    def bookItemSearch(self):
        bookItemList = []
        value = input("give an ISBN, Title or Author")
        with open("BookItemDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for r in csv_reader:
                bookItemList.append(BookItem(r[0], r[1], r[2], r[3]))

        for i in bookItemList:
            if value.lower() == i.ISBN.lower() or value.lower() == i.title.lower() or value.lower() == i.author.lower():
                print(i.__repr__())


