from .console_state import ConsoleState
from .book import Book
from .google_cloud_db import GoogleCloudDb

# Class is meant to represent the console state whilst the user is currently searching for a book
class SearchConsoleState(ConsoleState):

    def __init__(self, display_text):
        super().__init__(display_text, '')
        self.complete = False

    def handle_input(self, input_string, context):
        if self.complete is True:
            print("Your search has been completed.")
            #context...
            return 'main'
        elif(1<=int(input_string)<=4):
           #context...
           pass
        else: 
            print("Incorrect input.")

        return ''
    
    def display(self):
        if self.complete is True:
            print("Your search has been completed.")
        
        return input("Press 1 to search by BookID, 2 to search by Title, 3 to search by Author, or 4 to search by Date: ")

    def input(self):
        if self.complete is True:
            return input("Title/Name: ")

    

