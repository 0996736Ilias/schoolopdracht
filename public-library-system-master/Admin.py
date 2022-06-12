import csv
import json
import Book
from Person import Person
from BookItem import BookItem


class Admin(Person):
    """This is a Admin class"""

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
        try:
            int(self.number)
            print("[Member] Error no input")
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
                        print("[Admin] Deleting...")
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
                        print("[Admin] Deleted")
                    else:
                        tmp.append([r])

                writer.writerows(tmp)
        except:
            print("not an ID")


