from .console_state import ConsoleState

class ResultConsoleState(ConsoleState):

    def __init__(self, display_text, utility, gc):
        super().__init__(display_text, '')
        self.utility = utility
        self.gc = gc

    def input(self):
        while True:
            try:
                response = int(input(
                    """Please enter the number of the respective  
                    book that you wish to borrow: """))
                if 1 <= response <= len(self.utility.cur_results):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("That's not a valid option, please try again.")
        
        return response
        
    def handle_input(self, input_string, context):
        requested_book = context.cur_results[input_string-1]

        # if requested book is available AND 

        

        context.reset_results()
        return 'main'
        
    
    def display(self):
        for count,items in enumerate(self.utility.cur_results,1):
            print(count,items)