import unittest
from unittest import mock
from borrow_console_state import BorrowConsoleState
from utility import Utility
from google_cloud_db import GoogleCloudDb
from google_calendar import GoogleCalendar
from book import Book
from master_user import MasterUser

# Tests for borrow console state class
class TestBorrowConsoleState(unittest.TestCase):
	
	# Tests if the borrow again loops for both accepted responses
	def test_borrow_again(self):
		print('test borrow_again')
		gc = GoogleCalendar()
		gcdb = GoogleCloudDb()
		utility = Utility(gcdb, None)
		bcs = BorrowConsoleState(utility, gc)
		print('Assert if TRUE')
		self.assertTrue(bcs.borrow_again())
		print('Assert if FALSE')
		self.assertFalse(bcs.borrow_again())
	
	# Tests if the calc_dates runs properly
	def test_calc_dates(self):
		print('test calc_dates')
		gc = GoogleCalendar()
		gcdb = GoogleCloudDb()
		utility = Utility(gcdb, None)
		bcs = BorrowConsoleState(utility, gc)
		bcs.calc_dates()
		
	# Tests if borrow cs can display the appropriate message
	def test_display(self):
		print('test you must search first display')
		gc = GoogleCalendar()
		gcdb = GoogleCloudDb()
		utility = Utility(gcdb, None)
		bcs = BorrowConsoleState(utility, gc)
		bcs.display()
		
		# Test mocks a prior search result to test the display response
		print('testing with search first display')
		list = []
		book = Book(1, 'title', 'author', '12/09/99')
		list.append(book)
		utility.add_cur_results(list)
		bcs2 = BorrowConsoleState(utility, gc)
		bcs2.display()
		
		
	# Tests input by comparing mock book ID against response from borrow cs input method
	def test_input(self):
		print('test input')
		list = []
		gc = GoogleCalendar()
		gcdb = GoogleCloudDb()
		utility = Utility(gcdb, None)
		book = Book(1, 'title', 'author', '12/09/99')
		list.append(book)
		utility.add_cur_results(list)
		bcs = BorrowConsoleState(utility, gc)
		self.assertEqual(bcs.input().book_id,1)
	
	# Tests the handle input method is able to function entirely with mock user/book/list data
	def test_handle_input(self):
		print('test handle input')
		list = []
		gc = GoogleCalendar()
		gcdb = GoogleCloudDb()
		utility = Utility(gcdb, None)
		book = Book(1, 'title', 'author', '12/09/99')
		list.append(book)
		utility.add_cur_results(list)
		utility.user = MasterUser('username','firstname','lastname',1)
		bcs = BorrowConsoleState(utility, gc)
		bcs.handle_input(book, utility)
		
if __name__ == '__main__':
    unittest.main()
		
	