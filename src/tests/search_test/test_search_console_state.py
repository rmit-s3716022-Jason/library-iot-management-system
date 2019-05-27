import unittest
from unittest import mock
from console import Console
from search_console_state import SearchConsoleState
from utility import Utility
from google_cloud_db import GoogleCloudDb

# Tests for search console state class
class TestSearchConsoleState(unittest.TestCase):
	
	# Tests the scs is about to display the message
	def test_display(self):
		print('test display')
		scs = SearchConsoleState()
		scs.display()
	
	# Tests that the search console is about to take input
	def test_input(self):
		print('test input')
		scs = SearchConsoleState()
		scs.input()
	
	# Tests that the search console can handle the option of 1 (search by ID)
	def test_handle_input(self):
		print('test handle input')
		gcdb = GoogleCloudDb()
		utility = Utility(gcdb, None)
		scs = SearchConsoleState()
		scs.handle_input(1, utility)
		
if __name__ == '__main__':
    unittest.main()
		
	