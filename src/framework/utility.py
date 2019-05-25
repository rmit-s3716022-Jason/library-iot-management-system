class Utility:
    def __init__(self, db, socket):
        self.db = db
        self.socket = socket
        self.cur_results = []
        self.active_borrows = []
    
    def add_cur_results(self, results):
        self.cur_results.extend(results)

    def reset_results(self):
        self.cur_results.clear()

    def add_borrowing(self, borrow):
        self.active_borrows.append(borrow)
    
    def remove_borrowing(self, borrow):
        self.active_borrows.remove(borrow)
    


