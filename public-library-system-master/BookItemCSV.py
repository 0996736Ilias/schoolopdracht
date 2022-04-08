import csv
import Person
import BookItem
import BookJSON
from random import randint

bookItemCSV = "BookItemDatabase.csv"

def readFromBookItemCSV():
    bookItemList = []

    with open(bookItemCSV, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #line_count = 0

        for r in csv_reader:
            bookItemList.append( BookItem.BookItem(r[0], r[1], r[2], r[3]) )
            
    return bookItemList

def writeToBookItemCSV(row_contents):
    with open(bookItemCSV, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        writer.writerow(row_contents)





