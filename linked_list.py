class linked_list:
	def __init__(self, head=None):
		self._head = head
	
	def get_head(self):
		return self._head
		
	def set_head(self, head):
		self._head = head
	
class node:
	def __init__(self, data):
		self._data = data
		self._node = None
	
	def get_data(self):
		return self._data
	
	def get_next(self):
		return self._node
	
	def set_data(self, data):
		self._data = data
	
	def set_next(self, node):
		self._node = node
	
	