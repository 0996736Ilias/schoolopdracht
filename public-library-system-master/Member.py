import csv
from Person import Person


class Member(Person):
    """This is a Member class"""

    def writeToDatabase(self):
        row_contents = [self.number, self.givenName, self.surname,
                        self.streetAddress, self.zipCode, self.city, self.emailAddress, self.username, self.password,
                        self.telephonenumber]
        with open("PersonDatabase.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(row_contents)
        with open("MemberDatabase.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow([self.number])


    def delete(self):
        if self.number == '':
            print("[Member] Error no input")
        try:
            int(self.number)
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
                        print("[PersonCSV] Deleting")
                    else:
                        tmp.append(r.__repr__())
                tmp.pop(-1)
                writer.writerows(tmp)

            numberlist = []

            with open("MemberDatabase.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for r in csv_reader:
                    numberlist.append((r[0]))
            with open("MemberDatabase.csv", mode='w', newline='') as csv_file:
                tmp = []
                writer = csv.writer(csv_file)
                for r in numberlist:
                    if self.number == str(r[0]):
                        print("[Member] Deleting")
                    else:
                        a = [r]
                        tmp.append(a)
                tmp.pop(-1)
                writer.writerows(tmp)
        except:
            print("not an ID")