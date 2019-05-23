from .console_state import ConsoleState

# Class is meant to represent the console state whilst the user is currently
# searching for a book

class SearchConsoleState(ConsoleState):

    def __init__(self, display_text):
        super().__init__(display_text, '')
        self.options = ['BookID', 'Title', 'Author', 'Date']

    def input(self):
        while True:
            try:
                response = int(input(
                    """Enter '1' to search by BookID, '2' to search by Title,
                    '3' to search by Author,
                    or '4' to search by Date: """))
                if 1 <= response <= 4:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("That's not a valid option, please try again.")
        
        return response

    def handle_input(self, input_string, context):
        response = input('Please enter desired %s:' %
                            self.options[input_string-1])
        results = context.db.search(input_string, response)

        if results:
            print("Your search has been completed.")
            context.db.add_cur_results(results)
            return 'result'
        else:
            print('No results returned.')
            return 'main'

    def display(self):
        print('Book search.')
