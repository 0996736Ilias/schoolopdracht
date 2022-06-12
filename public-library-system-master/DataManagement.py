from datetime import datetime
import json
import csv
import os

class DataManagement():
    def backupMakeBookJSON(self, backupDirectory):
        with open("BookDatabase.json", "r") as read_file:
            jsonData = json.load(read_file)

        with open(str(backupDirectory) + "/BookDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".json",
                  'w+') as outfile:
            json.dump(jsonData, outfile, indent=4)


    def backupMakePersonCSV(self, backupDirectory):
        csvData = []
        with open("PersonDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                csvData.append(row)

        with open(str(backupDirectory) + "/PersonDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".csv", 'w+',
                  newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerows(csvData)


    def backupMakeMemberSCV(self, backupDirectory):
        csvData = []
        with open("MemberDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                csvData.append(row)

        with open(str(backupDirectory) + "/Member" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".csv", 'w+',
                  newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerows(csvData)


    def backupMakeLoanAdministrationSCV(self, backupDirectory):
        csvData = []
        with open("LoanAdministrationDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                csvData.append(row)

        with open(str(backupDirectory) + "/LoanAdministrationDatabase" + datetime.now().strftime(
                "%d-%b-%Y_%H-%M-%S") + ".csv", 'w+', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerows(csvData)


    def backupMakeAdminDatabaseSCV(self, backupDirectory):
        csvData = []
        with open("AdminDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                csvData.append(row)

        with open(str(backupDirectory) + "/LibrarianDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".csv", 'w+',
                  newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerows(csvData)


    def backupMakeBookitemDatabaseSCV(self, backupDirectory):
        csvData = []
        with open("BookItemDatabase.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                csvData.append(row)

        with open(str(backupDirectory) + "/BookItemDatabase" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S") + ".csv", 'w+',
                  newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerows(csvData)


    def backupRestorePersonCSV(self, folderName):
        fileName = os.listdir('./Backups/' + folderName)
        csvData = []
        with open('./Backups/' + folderName + "/" + fileName[4], mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                csvData.append(row)

        with open("PersonDatabase.csv", 'w+', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerows(csvData)


    def backupRestoreMemberCSV(self, folderName):
        fileName = os.listdir('./Backups/' + folderName)
        csvData = []
        with open('./Backups/' + folderName + "/" + fileName[5], mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                csvData.append(row)

        with open("MemberDatabase.csv", 'w+', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerows(csvData)


    def backupRestoreLoanAdministrationCSV(self, folderName):
        fileName = os.listdir('./Backups/' + folderName)
        csvData = []
        with open('./Backups/' + folderName + "/" + fileName[3], mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                csvData.append(row)

        with open("LoanAdministrationDatabase.csv", 'w+', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerows(csvData)


    def backupRestoreAdminDatabaseCSV(self, folderName):
        fileName = os.listdir('./Backups/' + folderName)
        csvData = []
        with open('./Backups/' + folderName + "/" + fileName[2], mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                csvData.append(row)

        with open("AdminDatabase.csv", 'w+', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerows(csvData)


    def backupRestoreBookItemDatabaseCSV(self, folderName):
        fileName = os.listdir('./Backups/' + folderName)
        csvData = []
        with open('./Backups/' + folderName + "/" + fileName[1], mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                csvData.append(row)

        with open("BookItemDatabase.csv", 'w+', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=',')
            writer.writerows(csvData)


    def backupRestoreBookJSON(self, folderName):
        fileName = os.listdir('./Backups/' + folderName)
        with open('./Backups/' + folderName + "/" + fileName[0]) as read_file:
            jsonData = json.load(read_file)

        with open("BookDatabase.json", "w") as outfile:
            json.dump(jsonData, outfile, indent=4)


    def loadInBookJSON(self):
        try:
            with open('./Data/' + 'Books.json') as read_file:
                jsonData = json.load(read_file)

            with open("BookDatabase.json", "w") as outfile:
                json.dump(jsonData, outfile, indent=4)
        except:
            print('[Loadfile] error file not found')


    def loadInUsers(self):
        try:
            csvData = []
            with open('./Data/' + "Person.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:
                    csvData.append(row)

            with open("PersonDatabase.csv", 'w+', newline='') as outfile:
                writer = csv.writer(outfile, delimiter=',')
                writer.writerows(csvData)
            csvData = []
            with open('./Data/' + "Admin.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:
                    csvData.append(row)

            with open("AdminDatabase.csv", 'w+', newline='') as outfile:
                writer = csv.writer(outfile, delimiter=',')
                writer.writerows(csvData)
            csvData = []
            with open('./Data/' + "Member.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:
                    csvData.append(row)

            with open("MemberDatabase.csv", 'w+', newline='') as outfile:
                writer = csv.writer(outfile, delimiter=',')
                writer.writerows(csvData)
        except:
            print('[Loadfile] error file not found')


    def addListOfBooks(self):
        print("Looking for file Books.json in /DataTOAdd")
        try:
            with open("BookDatabase.json", "r") as read_file:
                jsonData = json.load(read_file)

            with open('./DataToAdd/' + 'Books.json') as read_file:
                a = json.load(read_file)
            jsonData.append(a)
            with open("BookDatabase.json", "w") as outfile:
                json.dump(jsonData, outfile, indent=4)
            print("Books added")
        except:
            print('[Loadfile] error file not found')


    def addListOfUsers(self):
        try:
            csvData = []

            with open("PersonDatabase.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:
                    csvData.append(row)
            with open('./DataToAdd/' + "Person.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:
                    csvData.append(row)

            with open("PersonDatabase.csv", 'w+', newline='') as outfile:
                writer = csv.writer(outfile, delimiter=',')
                writer.writerows(csvData)

            csvData = []
            with open("AdminDatabase.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:
                    csvData.append(row)
            with open('./DataToAdd/' + "Admin.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:
                    csvData.append(row)

            with open("AdminDatabase.csv", 'w+', newline='') as outfile:
                writer = csv.writer(outfile, delimiter=',')
                writer.writerows(csvData)
            csvData = []
            with open("MemberDatabase.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:
                    csvData.append(row)

            with open('./DataToAdd/' + "Member.csv", mode='r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                for row in csv_reader:
                    csvData.append(row)

            with open("MemberDatabase.csv", 'w+', newline='') as outfile:
                writer = csv.writer(outfile, delimiter=',')
                writer.writerows(csvData)

        except:
            print("error")


    def backupMake(self):
        path = "Backups/Backup_" + datetime.now().strftime("%d-%b-%Y_%H-%M-%S")
        os.mkdir(path)
        self.backupMakeBookJSON(path)
        self.backupMakePersonCSV(path)
        self.backupMakeMemberSCV(path)
        self.backupMakeLoanAdministrationSCV(path)
        self.backupMakeAdminDatabaseSCV(path)
        self.backupMakeBookitemDatabaseSCV(path)
        print(
            "[Backup]\n[Backup] Backup has been made with date: " + datetime.now().strftime("%d-%b-%Y_%H-%M-%S\n[Backup]"))


    def backupRestore(self, folderName):
        self.backupRestoreBookJSON(folderName)
        self.backupRestorePersonCSV(folderName)
        self.backupRestoreMemberCSV(folderName)
        self.backupRestoreLoanAdministrationCSV(folderName)
        self.backupRestoreAdminDatabaseCSV(folderName)
        self.backupRestoreBookItemDatabaseCSV(folderName)


    def backupRestoreMenu(self):
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
                folderName = backupFile[int(backupSelectOption) - 1]
                inRestoreMenu = False
                self.backupRestore(folderName)
            else:
                print("[Backup] Invalid input. Please try again.")
