class linked_list:
	def __init__(self, head=None):
		self._head = head

	def get_head(self):
		return self._head

	def set_head(self, head):
		self._head = head

	def add_node_to_tail(self, node):
		curr = self._head
		while curr.get_next() is not None:
			curr = curr.get_next()
		curr.set_next(node)
		return

	def add_node_to_head(self, node):
		prev_head = self._head
		self._head = node
		node.set_next(prev_head)
		return

	def delete_node(self, start, data):
		curr = self.get_head()
		if start == curr:
			self.set_head(curr.get_next())
			return
		while curr != start and curr is not None:
			prev = curr
			curr = curr.get_next()
		if curr is None:
			print("Error: node not in the linked list")
			return
		while curr is not None:
			if curr.get_data() == data:
				prev.set_next(curr.get_next())
				return
			curr = curr.get_next()

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
