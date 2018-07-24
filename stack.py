class stack:
	def __init__(self):
		self._top = None
		self._prev_min = None
	
	def top(self):
		if self._top is None:
			return 
		return self._top.get_data()
	
	def is_empty(self):
		if self._top is None:
			return True
		return False
	
	def push(self, data):
		item = node(data)
		if self.is_empty():
			item.set_stack_min(item.get_data())
			self._prev_min = item.get_data()
		if item.get_data() < self._prev_min:
			item.set_stack_min(item.get_data())
			self._prev_min = item.get_data()
		else:
			item.set_stack_min(self._prev_min)
		item.set_next(self._top)
		self._top = item
		
	def pop(self):
		if self.is_empty():
			return None
		item = self._top
		self._top = self._top.get_next()
		return item.get_data()
	
	def find_min(self):
		if self.is_empty():
			return None
		item = self._top
		return item.get_stack_min()
		
class node:
	def __init__(self, data, stack_min=None):
		self._data = data
		self._node = None
		self._stack_min = None
	
	def get_data(self):
		return self._data
	
	def get_next(self):
		return self._node
	
	def get_stack_min(self):
		return self._stack_min
	
	def set_data(self, data):
		self._data = data
	
	def set_next(self, node):
		self._node = node
	
	def set_stack_min(self, stack_min):
		self._stack_min = stack_min