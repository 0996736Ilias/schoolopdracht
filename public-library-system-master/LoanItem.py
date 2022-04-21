import csv
import BookItem


class LoanItem():
    """This is a LoanItem class"""

    def __init__(self, subscriberNumber, days, ISBN):
        self.subscribernumber = subscriberNumber
        self.days = days
        self.ISBN = ISBN
    def __repr__(self):
        return str(self.subscribernumber) + ", "+ self.days+ ", "+self.ISBN

    def writeToDatabase(self):
        with open("LoanAdministrationDatabase.csv", 'a', newline='') as write_obj:
            #  Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            #  Add contents of list as last row in the csv file
            contentList = [self.subscribernumber, self.days, self.ISBN]
            csv_writer.writerow(contentList)




def returnItem(ISBN):
    a = 0
    list = readFromLoanItemCSV()
    with open(loanItemCSV, mode='r+', newline='') as csv_file:
        tmp = []

        writer = csv.writer(csv_file)
        for r in list:
            if ISBN == r.ISBN and a == 0:
                a = a + 1
                print("[LoanItem] SKIP")
            else:
                tmp.append(r.__repr__())
        print(tmp)
        tmp.pop(-1)
        writer.writerows(tmp)






loanItemCSV = "loanAdministrationDatabase.csv"


def readFromLoanItemCSV():
    loanItemList = []

    with open(loanItemCSV, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for r in csv_reader:
            loanItemList.append(LoanItem(r[0], r[1], r[2]))
    return loanItemList


def writeToLoanItemCSV(row_contents):
    with open(loanItemCSV, 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(row_contents)


def loanedToPerson(ID):
    loanedlist = readFromLoanItemCSV()
    catalog = BookItem.readFromBookItemCSV()
    for j in loanedlist:
        if j.subscribernumber == str(ID):
            for i in catalog:
                if (j.ISBN == i.ISBN):
                    print(i)

def limitCheck(ID):
    loanedlist = readFromLoanItemCSV()
    a = 0
    for j in loanedlist:
        if j.subscribernumber == ID:
            a = a + 1
    if a >= 3:
        return False
    return True
