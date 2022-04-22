import csv
import BookItem


class LoanItem():
    """This is a LoanItem class"""

    def __init__(self, subscriberNumber, days, ISBN):
        self.subscribernumber = subscriberNumber
        self.days = days
        self.ISBN = ISBN

    def __repr__(self):
        return str(self.subscribernumber), self.days, self.ISBN

    def writeToDatabase(self):
        with open("LoanAdministrationDatabase.csv", 'a', newline='') as write_obj:
            #  Create a writer object from csv module
            csv_writer = csv.writer(write_obj)
            #  Add contents of list as last row in the csv file
            contentList = [self.subscribernumber, self.days, self.ISBN]
            csv_writer.writerow(contentList)

    def returnItem( self, CURRENTUSER):
        a = 0
        list = LoanItem.readFromLoanItemCSV()
        with open("loanAdministrationDatabase.csv", mode='w', newline='') as csv_file:
            tmp = []

            writer = csv.writer(csv_file)
            for r in list:
                if self.ISBN == r.ISBN and a == 0 and r.subscribernumber == CURRENTUSER:
                    a = a + 1
                    print("[LoanItem] SKIP")
                else:
                    tmp.append(r.__repr__())
            print(tmp)
            writer.writerows(tmp)

    def loanAvailabilityCheck( ISBN, author, title):

        copiesCount = 0
        copies = 0
        for book in BookItem.BookItem.readFromBookItemCSV():
            if author == book.author and title == book.title:
                copies = int(book.copies)

        for loanItem in LoanItem.readFromLoanItemCSV():
            if ISBN == loanItem.ISBN:
                copiesCount += 1

        if copies - copiesCount > 0:
            return True
        else:
            return False

    def readFromLoanItemCSV():
        loanItemList = []

        with open("loanAdministrationDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for r in csv_reader:
                loanItemList.append(LoanItem(r[0], r[1], r[2]))
        return loanItemList

    def loanedToPerson( ID):
        loanedlist = LoanItem.readFromLoanItemCSV()
        catalog = BookItem.BookItem.readFromBookItemCSV()
        for j in loanedlist:
            if j.subscribernumber == str(ID):
                for i in catalog:
                    if (j.ISBN == i.ISBN):
                        print(i)

    def limitCheck( ID):
        loanedlist = LoanItem.readFromLoanItemCSV()
        a = 0
        for j in loanedlist:
            if j.subscribernumber == ID:
                a = a + 1
        if a >= 3:
            return False
        return True
