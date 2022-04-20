import csv
import LoanItem
import BookItemCSV

loanItemCSV = "loanAdministrationDatabase.csv"


def readFromLoanItemCSV():
    loanItemList = []

    with open(loanItemCSV, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for r in csv_reader:
            loanItemList.append(LoanItem.LoanItem(r[0], r[1], r[2]))
    return loanItemList


def writeToLoanItemCSV(row_contents):
    with open(loanItemCSV, 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(row_contents)


def loanedToPerson(ID):
    loanedlist = readFromLoanItemCSV()
    catalog = BookItemCSV.readFromBookItemCSV()
    for j in loanedlist:
        if j.subscribernumber == str(ID):
            for i in catalog:
                if (j.ISBN == i.ISBN):
                    print(i)
