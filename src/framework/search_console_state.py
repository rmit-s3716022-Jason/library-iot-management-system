from .console_state import ConsoleState
from .book import Book
from .google_cloud_db import GoogleCloudDb

# Class is meant to represent the console state whilst the user is currently searching for a book
class SearchConsoleState(ConsoleState):

    def __init__(self):
        super().__init__('', '')
        self.complete = False

    def handle_input(self, input_string, context):
        
        
        pass
    
    def display(self):
        if self.complete is True:
            print("Your search has been completed.")
        
        return input("Press 1 to search by BookID, 2 to search by Title, 3 to search by Author, or 4 to search by Date: ")

    def input(self):
        if self.complete is True:
            return input("Title/Name: ")

    

