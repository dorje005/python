class binary_tree:
	def __init__(self, root=None):
		self._root = root
	
	def get_root(self):
		return self._root
	
	def set_root(self, root):
		self._root = root
	
	def insert_node(self, node):
		if self._root == None:
			self._root = node
			return
		curr = self._root
		while curr is not None:
			prev = curr
			if curr.get_data() > node.get_data():
				curr = curr.get_left()
				if curr is None:
					prev.set_left(node)
			else: 
				curr = curr.get_right()
				if curr is None:
					prev.set_right(node)
	
	def delete_node(self, node): 
		if self._root == None:
			return 
		if self._root.get_data() == node.get_data():
			self._root = delete_root(self._root)
		curr = self._root
		while curr is not None and curr.get_data() == node.get_data():
			prev = curr
			if curr.get_data() > node.get_data():
				curr = curr.get_left()
			else:
				curr = curr.get_right()
		if curr is not None:
			delete_root(curr)
	
	def delete_root(self, root):
		root_left = root.get_left()
		root_right = root.get_right()
		if root_left is not None:
			if root_left.get_right() is not None:
				new_right = root_left.get_right()
				while new_right.get_right() is not None:
					new_right = new_right.get_right()
				new_right.set_right(root_right)
			return root_left
		else:
			return root_right
		
class node:
	def __init__(self, data):
		self._data = data 
		self._left = None
		self._right = None

	def get_data(self):
		return self._data 
	
	def get_left(self):
		return self._left
	
	def get_right(self):
		return self._right
	
	def set_data(self, data):
		self._data = data 
	
	def set_left(self, left):
		self._left = left
	
	def set_right(self, right):
		self._right = right