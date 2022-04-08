import csv

class Librarian():  
    """This is a Librarian class"""
    def __init__(self, number):
        self.number = number

    def writeToDatabase(self):
        with open("LibrarianDatabase.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow([self.number])

def readFromLibrarianCSV():
    numberList = []

    with open ("LibrarianDatabase.csv", mode ='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for r in csv_reader:
            numberList.append( (r[0]) )

    return numberList

def librarianCheck(number):
    numberList = readFromLibrarianCSV()
    if number in numberList:
        return True
