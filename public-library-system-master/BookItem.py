import csv


class BookItem():
    """This is a BookItem class"""

    def __init__(self, title, author, copies, ISBN):
        self.title = title
        self.author = author
        self.copies = copies
        self.ISBN = ISBN

    def __repr__(self):
        return [self.title, self.author, self.copies, self.ISBN]

    def writeToDatabase(self):
        row_contents = [self.title, self.author, self.copies, self.ISBN]

        with open(bookItemCSV, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            writer.writerow(row_contents)

    def deleteBookItem(self):
        bookItemList = []

        with open("BookItemDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for r in csv_reader:
                bookItemList.append(BookItem(r[0], r[1], r[2], r[3]))

        with open("BookItemDatabase.csv", mode='w', newline='') as csv_file:
            tmp = []
            writer = csv.writer(csv_file)
            for r in bookItemList:
                if self.ISBN == r.ISBN:
                    print(r.__repr__())
                    print("[BookItem] deleting...")
                else:
                    tmp.append(r.__repr__())
            print(tmp)

            writer.writerows(tmp)

    def editBookItem(self):
        bookItemList = []

        with open("BookItemDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for r in csv_reader:
                bookItemList.append(BookItem(r[0], r[1], r[2], r[3]))

        with open("BookItemDatabase.csv", mode='w', newline='') as csv_file:
            tmp = []
            writer = csv.writer(csv_file)
            for r in bookItemList:
                if self.ISBN == r.ISBN:
                    print(r.__repr__())
                    r.title = input("Give name")
                    r.author = input("Give author")
                    r.copies = input("Give copies")
                    print("[BookItem] editing...")
                    print(r.__repr__())
                    tmp.append(r.__repr__())
                else:
                    tmp.append(r.__repr__())
            print(tmp)
            writer.writerows(tmp)


bookItemCSV = "BookItemDatabase.csv"


def readFromBookItemCSV():
    bookItemList = []

    with open(bookItemCSV, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for r in csv_reader:
            bookItemList.append(BookItem(r[0], r[1], r[2], r[3]))

    return bookItemList


def bookItemSearch(value):
    list = readFromBookItemCSV()
    for i in list:
        if value == i.ISBN or value == i.title or value == i.author:
            print(i)
