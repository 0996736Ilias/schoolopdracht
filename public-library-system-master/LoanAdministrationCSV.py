import csv
import LoanItem

loanItemCSV = "loanAdministrationDatabase.csv"

def readFromLoanItemCSV():
    loanItemList = []

    with open(loanItemCSV, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for r in csv_reader:
            loanItemList.append( LoanItem.LoanItem(r[0], r[1], r[2]) )
            
    return loanItemList

def writeToLoanItemCSV(row_contents):
    with open(loanItemCSV, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row_contents)