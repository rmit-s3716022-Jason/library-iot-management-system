import unittest
from unittest import mock
from mock_state import MockState
from console import Console

# Unit test tests the functionality of the console class
class TestConsole(unittest.TestCase):
    
    def test_add_state(self):
        print('test add_state')
        console = Console(None)
        mock_state = mock.Mock()
        console.add_state('mock', mock_state)
    
    def test_set_current_state(self):
        print('test set current state')
        console = Console(None)
        mock_state = mock.Mock()
        console.add_state('mock', mock_state)
        console.set_current_state('mock')
       

    def test_run(self):
        print('test run')
        console = Console(None)
        mock_state = MockState()
        console.add_state('mock', mock_state)
        console.set_current_state('mock')
        console.run()
        
if __name__ == '__main__':
    unittest.main()
