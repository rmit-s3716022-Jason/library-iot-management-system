from .console_state import ConsoleState
from .book import Book
from .google_cloud_db import GoogleCloudDB


class SearchConsoleState(ConsoleState, GoogleCloudDB):
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
        instance of GoogleCloudDB class is created and stored in db
        db is used to access data from the google cloud database
        a list is then generated from the function and looped through
        """
        db = GoogleCloudDB()
        db.load_books()
        for i in GoogleCloudDB.books:
            if input_string == i.title:
                print("An excellent read!\nBookID: ", i.book_id)
                print("\nTitle", i.title)
                print("\nAuthor", i.author)
                self.complete == True
                return 'done'
            elif input_string == i.author:
                print("An excellent read!\nBookID: ", i.book_id)
                print("\nTitle", i.title)
                print("\nAuthor", i.author)
                self.complete == True
                return 'done'
            elif input_string == i.book_id:
                print("An excellent read!\nBookID: ", i.book_id)
                print("\nTitle", i.title)
                print("\nAuthor", i.author)
                self.complete == True
                return 'done'
            elif input_string == i.published_date:
                print("An excellent read!\nBookID: ", i.book_id)
                print("\nTitle", i.title)
                print("\nAuthor", i.author)
                self.complete == True
                return 'done'
            else:
                print("Cannot find the book you're looking, please check your spelling")
                return 'done'      

    def display(self):
        """
        checks if boolean complete has been triggered and sends a message
        default message is sent regardless
        """
        if self.complete == True:
            print("You've completed a search")
        print("Search our database using either the name of the author or the title of the book!")

    def input(self):
        """
        checks if boolean complete has been triggered
        """
        if self.complete == False:
            return input("Title/Name: ")
        
        
