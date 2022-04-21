import csv
from Person import Person


class Librarian(Person):
    """This is a Librarian class"""

    def writeToDatabase(self):
        row_contents = [self.number, self.givenName, self.surname,
                        self.streetAddress, self.zipCode, self.city, self.emailAddress, self.username, self.password,
                        self.telephonenumber]

        with open("PersonDatabase.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(row_contents)
        with open("LibrarianDatabase.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow([self.number])

    def delete(self, number):
        with open("PersonDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            List = []
            for r in csv_reader:
                List.append(Person(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]))

        with open("PersonDatabase.csv", mode='r+', newline='') as csv_file:
            tmp = []
            writer = csv.writer(csv_file)
            for r in List:
                if str(number) == r.number:
                    print("[PersonCSV] SKIP")
                else:
                    tmp.append(r.__repr__())
            print(tmp)
            tmp.pop(-1)
            writer.writerows(tmp)

        numberlist = []

        with open("LibrarianDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for r in csv_reader:
                numberlist.append((r[0]))
        with open("LibrarianDatabase.csv", mode='r+', newline='') as csv_file:
            tmp = []
            writer = csv.writer(csv_file)
            for r in numberlist:
                if self.number == r[0]:
                    print("[Librarian] SKIP")
                else:
                    tmp.append(r.__repr__())
            print(tmp)
            tmp.pop(-1)
            writer.writerows(tmp)

    def editPerson(self, number):
        with open("PersonDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            list = []
            for r in csv_reader:
                list.append(Person(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9]))
        with open("PersonDatabase.csv", mode='r+', newline='') as csv_file:
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
