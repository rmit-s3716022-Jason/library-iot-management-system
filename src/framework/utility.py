class Utility:
    def __init__(self, db, socket):
        self.db = db
        self.socket = socket
        self.cur_results = []
    
    def add_cur_results(self, results):
        self.cur_results.extend(results)

    def reset_results(self):
        self.cur_results.clear()
    
    def remove_result(self, item):
        self.cur_results.remove(item)



