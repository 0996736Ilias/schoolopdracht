import csv
import csv
import Person

personCSV = "PersonDatabase.csv"


def readFromPersonCSV():
    with open(personCSV, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        List = []
        for r in csv_reader:
            List.append(Person.Person(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]))
    return List


def writeToPersonCSV(row_contents):
    with open(personCSV, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row_contents)

def deletePerson(username):
    with open(personCSV, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
           if row[0] == username:
               print('p')
               row[7] = "Null"

@