import csv
import json
class Person(object):
    """This is a person class"""

    def __init__(self, number, givenname, surname, streetaddress,
                 zipcode, city, emailAddress, username, password, telephonenumber):
        self.number = number
        self.givenName = givenname
        self.surname = surname
        self.streetAddress = streetaddress
        self.zipCode = zipcode
        self.city = city
        self.emailAddress = emailAddress
        self.username = username
        self.password = password
        self.telephonenumber = telephonenumber

    def __int__(self, number):
        self.number = number

    def __repr__(self):
        return [self.number, self.givenName, self.surname, self.streetAddress, self.zipCode, self.city,
                self.emailAddress, self.username, self.password, self.telephonenumber]

    def writeToDatabase(self):
        row_contents = [self.number, self.givenName, self.surname,
                        self.streetAddress, self.zipCode, self.city, self.emailAddress, self.username, self.password,
                        self.telephonenumber]

        with open("PersonDatabase.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(row_contents)

    def bookList(self):
        with open("BookDatabase.json", "r") as read_file:
            data = json.load(read_file)

        for row in data:
            print(row)




