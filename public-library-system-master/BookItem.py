import csv
import BookItemCSV

class BookItem():  
    """This is a BookItem class"""
    def __init__(self, title, author, copies, ISBN):
        self.title = title
        self.author = author
        self.copies = copies
        self.ISBN = ISBN

 
    def writeToDatabase(self):
        row_contents = [self.title, self.author, self.copies, self.ISBN]
        
        BookItemCSV.writeToBookItemCSV(row_contents)


