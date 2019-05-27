"""
search_console_state.py
=======================
"""


class SearchConsoleState():
    """
    Class is meant to represent the console state whilst the user is currently
    searching for a book
    """

    def __init__(self):
        self.options = ['BookID', 'Title', 'Author', 'Date']

    def input(self):
        while True:
            try:
                response = int(input("Enter option here: "))
                if 1 <= response <= 4:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("That's not a valid option, please try again.")
        
        return response

    def handle_input(self, input_string, context):
        response = input('Please enter desired %s: ' %
                            self.options[input_string-1])
        results = context.db.search(input_string, response)

        if results:
            print("Your search has been completed.")
            context.add_cur_results(results)
        else:
            print('No results returned.')

    def display(self):
        print('\nSearch book.')
        print("Select one of the following: ")
        print("""1. to search by BookID\n2. to search by Title\n3. to search by Author\n4. to search by Date.""")
