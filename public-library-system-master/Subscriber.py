import csv
from Person import Person

class Subscriber(Person):
    """This is a Subscriber class"""

    def writeToDatabase(self):
        with open("SubscriberDatabase.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow([self.number])


def readFromSubscriberCSV():
    numberList = []

    with open("SubscriberDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for r in csv_reader:
            numberList.append((r[0]))

    return numberList


def SubscriberCheck(number):
    numberList = readFromSubscriberCSV()
    if number in numberList:
        return True
