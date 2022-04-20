import csv
import BookItem

bookItemCSV = "BookItemDatabase.csv"


def readFromBookItemCSV():
    bookItemList = []

    with open(bookItemCSV, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # line_count = 0

        for r in csv_reader:
            bookItemList.append(BookItem.BookItem(r[0], r[1], r[2], r[3]))

    return bookItemList


def writeToBookItemCSV(row_contents):
    with open(bookItemCSV, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        writer.writerow(row_contents)


def readFromBookItemCSV():
    bookItemList = []

    with open(bookItemCSV, mode='r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for r in csv_reader:
            bookItemList.append(BookItem.BookItem(r[0], r[1], r[2], r[3]))

    return bookItemList


def deleteBookItem(ID):
    list = readFromBookItemCSV()

    with open(bookItemCSV, mode='r+', newline='') as csv_file:
        tmp = []
        writer = csv.writer(csv_file)
        for r in list:
            if ID == r.ISBN:
                print("[BookItem] deleting...")
            else:
                tmp.append(r.__repr__())
        print(tmp)
        tmp.pop(-1)
        writer.writerows(tmp)


def editBookItem(ID):
    list = readFromBookItemCSV()

    with open(bookItemCSV, mode='r+', newline='') as csv_file:
        tmp = []
        writer = csv.writer(csv_file)
        for r in list:
            if ID == r.ISBN:
                r.title = input("Give name")
                r.author = input("Give author")
                r.copies = input("Give copies")
            else:
                tmp.append(r.__repr__())
        print(tmp)
        tmp.pop(-1)
        writer.writerows(tmp)
