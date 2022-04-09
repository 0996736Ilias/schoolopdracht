import csv
import Person

personCSV = "PersonDatabase.csv"


def readFromPersonCSV():
    with open(personCSV, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        List = []
        for r in csv_reader:
            List.append(Person.Person(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]))
            print(r)
    return List


def writeToPersonCSV(row_contents):
    with open(personCSV, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row_contents)

def deletePerson(username):
    list = readFromPersonCSV()
    with open(personCSV, mode='r+', newline='') as csv_file:
        tmp = []
        writer = csv.writer(csv_file)
        for r in list:
            if username == r.number:
                r.givenName = ''
                r.surname = ''
                r.streetAddress = ''
                r.zipCode = ''
                r.city = ''
                r.emailAddress = ''
                r.username = ''
                r.password = ''
                r.telephonenumber = ''
                tmp.append(r.__repr__())
            else:
                tmp.append(r.__repr__())
        print(tmp)
        tmp.pop(-0)
        writer.writerows(tmp)

