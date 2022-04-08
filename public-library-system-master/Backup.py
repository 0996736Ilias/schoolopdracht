from datetime import datetime
import json
import Book
import csv
import os 

def backupMakeBookJSON(backupDirectory):
    with open ("BookDatabase.json", "r") as read_file:
        jsonData = json.load(read_file)

    with open(str(backupDirectory) + "/BookDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".json", 'w+') as outfile:
        json.dump(jsonData, outfile, indent = 4)     

def backupMakePersonCSV(backupDirectory):
    csvData = []
    with open("PersonDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            csvData.append(row)


    with open(str(backupDirectory) + "/PersonDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData)

def backupMakeSubscriberSCV(backupDirectory):
    csvData = []
    with open("SubscriberDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open(str(backupDirectory) + "/Subscriber" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData)

def backupMakeLoanAdministrationSCV(backupDirectory):
    csvData = []
    with open("LoanAdministrationDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open(str(backupDirectory) + "/LoanAdministrationDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData)

def backupMakeLibrarianDatabaseSCV(backupDirectory):
    csvData = []
    with open("LibrarianDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open(str(backupDirectory) + "/LibrarianDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData)

def backupMakeBookitemDatabaseSCV(backupDirectory):
    csvData = []
    with open("BookItemDatabase.csv", mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open(str(backupDirectory) + "/BookItemDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData)

def backupRestorePersonCSV(folderName):
    fileName = os.listdir('./Backups/' + folderName)
    csvData = []
    with open('./Backups/' + folderName + "/" + fileName[4], mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open("PersonDatabase.csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData)  

def backupRestoreSubscriberCSV(folderName):
    fileName = os.listdir('./Backups/' + folderName)
    csvData = []
    with open('./Backups/' + folderName + "/" + fileName[5], mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open("SubscriberDatabase.csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData) 

def backupRestoreLoanAdministrationCSV(folderName):
    fileName = os.listdir('./Backups/' + folderName)
    csvData = []
    with open('./Backups/' + folderName + "/" + fileName[3], mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open("LoanAdministrationDatabase.csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData) 

def backupRestoreLibrarianDatabaseCSV(folderName):
    fileName = os.listdir('./Backups/' + folderName)
    csvData = []
    with open('./Backups/' + folderName + "/" + fileName[2], mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open("LibrarianDatabase.csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData) 

def backupRestoreBookItemDatabaseCSV(folderName):
    fileName = os.listdir('./Backups/' + folderName)
    csvData = []
    with open('./Backups/' + folderName + "/" + fileName[1], mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
           csvData.append(row)

    with open("BookItemDatabase.csv", 'w+', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerows(csvData) 

def backupRestoreBookJSON(folderName):
    fileName = os.listdir('./Backups/' + folderName)
    with open ('./Backups/' + folderName + "/" + fileName[0]) as read_file:
        jsonData = json.load(read_file)

    with open("BookDatabase.json", "w") as outfile:
        json.dump(jsonData, outfile, indent = 4)     

def backupMake():
    path = "Backups/Backup_" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S")
    os.mkdir(path)
    backupMakeBookJSON(path)
    backupMakePersonCSV(path)
    backupMakeSubscriberSCV(path)
    backupMakeLoanAdministrationSCV(path)
    backupMakeLibrarianDatabaseSCV(path)
    backupMakeBookitemDatabaseSCV(path)
    print("[Backup]\n[Backup] Backup has been made with date: " + datetime.now().strftime("%d-%b-%Y_%H-%M-%S\n[Backup]"))
    
def backupRestore(folderName):
    backupRestoreBookJSON(folderName)
    backupRestorePersonCSV(folderName)
    backupRestoreSubscriberCSV(folderName)
    backupRestoreLoanAdministrationCSV(folderName)
    backupRestoreLibrarianDatabaseCSV(folderName)
    backupRestoreBookItemDatabaseCSV(folderName)

def backupRestoreMenu():
    inRestoreMenu = True
    while inRestoreMenu:
        iteration = 1
        optionList = []
        backupFile = os.listdir('./Backups')
        print("[Backup] ------------------------------------")
        print("[Backup] Select which backup you would like to restore")
        for file in backupFile:
            print("[Backup] " + str(iteration) + " - " + file)
            optionList.append(iteration)
            iteration += 1       
            
        print("[Backup] ")
        print("[Backup] Press 'q' to go back")
        print("[Backup] ")
        backupSelectOption = input("[Backup] Selection: ")

        if backupSelectOption == "q":
            inRestoreMenu = False
        elif int(backupSelectOption) in optionList:
            print("[Backup]")
            print("[Backup] Restored Successful")
            print("[Backup]")
            folderName = backupFile[int(backupSelectOption)-1]
            inRestoreMenu = False
            backupRestore(folderName)            
        else:
            print("[Backup] Invalid input. Please try again.")

