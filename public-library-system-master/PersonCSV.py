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
    list = readFromPersonCSV()
    with open(personCSV, mode='r+', newline='') as csv_file:
        tmp = []
        writer = csv.writer(csv_file)
        for r in list:
            if username == r.number:
                print("[PersonCSV] SKIP")
            else:
                tmp.append(r.__repr__())
        print(tmp)
        tmp.pop(-1)
        writer.writerows(tmp)

def editPerson(number):
    list = readFromPersonCSV()
    with open(personCSV, mode='r+', newline='') as csv_file:
        tmp = []
        writer = csv.writer(csv_file)
        for r in list:
            if number == r.number:
                r.givenName = input("Given name")
                r.surname = input("Sur name")
                r.streetAddress = input("Street Address")
                r.zipCode = input("Zip Code")
                r.city = input("City")
                r.emailAddress = input("Email")
                r.username = input("User name")
                r.password = input("Password")
                r.telephonenumber = input("telephone number")
                tmp.append(r.__repr__())
            else:
                tmp.append(r.__repr__())
        writer.writerows(tmp)