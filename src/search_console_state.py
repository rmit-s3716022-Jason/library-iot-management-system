from .console_state import ConsoleState
from .book import Book
from .google_cloud_db import GoogleCloudDB


class SearchConsoleState(ConsoleState):
    """
    this class is represents the console state while user is searching for a book 
    """

    def __init__(self):
        """
        Constructor: Creates the variables associated with this class
         
        :type display_text: string
        :param display_text: message that is display to the user

        :type prompt_text: string
        :param prompt_text: message this prompts the user to an action
        """
        
        super().__init__('', '')
        
        self.complete = False 


    def handle_input(self, input_string, context):
        """
        checks if boolean complete has been triggered and sends a message
        default message is sent regardless
        """
        if self.complete == True:
            print("You've completed a search")
        
        if input_string == "1":
            input_insert = 1
        elif input_string == "2":
             input_insert = 2
        elif input_string == "3":
             input_insert = 3
        elif input_string == "4":
            input_insert = 4
        else:
             print("Incorrect input")
        GoogleCloudDB.search_books(input_insert)
        return 'done' 
             

    def display(self):
        """
        checks if boolean complete has been triggered and sends a message
        default message is sent regardless
        """
        if self.complete == True:
            print("You've completed a search")

        input("Press 1 to search by BookID, press 2 search by Title, Press 3 search by Author, Press 4 search by Date")


    def input(self):
        """
        checks if boolean complete has been triggered
        """
        if self.complete == False:
            return input("Title/Name: ")
        
        
        
