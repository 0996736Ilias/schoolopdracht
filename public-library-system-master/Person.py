import PersonCSV
import Librarian
import Subscriber

class Person():  
    """This is a person class"""
    def __init__(self, number, givenname, surname, streetaddress,
    zipcode, city, emailAddress, username, password,  telephonenumber):
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

    def __repr__(self):
        return [self.number,  self.givenName, self.surname, self.streetAddress, self.zipCode, self.city, self.emailAddress, self.username, self.password, self.telephonenumber]




    def writeToDatabase(self, personType):
        row_contents = [self.number,  self.givenName, self.surname,
        self.streetAddress, self.zipCode, self.city, self.emailAddress, self.username, self.password, self.telephonenumber]
        
        PersonCSV.writeToPersonCSV(row_contents)
        self.librarianOrSubscriber(personType)

    def librarianOrSubscriber(self, personType):
        if personType == "librarian":
            librarian = Librarian.Librarian(self.number)
            librarian.writeToDatabase()
        else:
            subscriber = Subscriber.Subscriber(self.number)
            subscriber.writeToDatabase()
            
