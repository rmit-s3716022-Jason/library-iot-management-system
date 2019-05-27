class MockState:
	
	def display(self):
		return ''
	
	def input(self):
		return 1
		
	def handle_input(self,input_string, context):
		return 'exit'