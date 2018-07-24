def size(linked_list):
	head = linked_list.get_head()
	i = 0
	while head is not None:
		i = i + 1
		head = head.get_next()
	return i

def print_list(linked_list):
	head = linked_list.get_head()
	while head is not None:
		print(head.get_data(), end= " ")
		head = head.get_next()
	print("")

def delete_duplicates(linked_list):
	if size(linked_list) <= 1:
		return linked_list
	curr_head = linked_list.get_head()
	while curr_head is not None:
		curr_data = curr_head.get_data()
		start = curr_head.get_next()
		while start is not None:
			if start.get_data() == curr_data:
				linked_list.delete_node(start, curr_data)
			start = start.get_next()
		curr_head = curr_head.get_next()
	return linked_list

def insertion_sort_linked_list(linked_list):
	if size(linked_list) == 0:
		return linked_list
	curr_node = linked_list.get_head()
	curr_pos = 0
	while curr_node is not None:
		must_swap = False
		min_pos = curr_pos
		min_value = curr_node.get_data()
		iter = curr_node.get_next()
		i = curr_pos + 1
		while iter is not None:
			if iter.get_data() < min_value:
				min_value = iter.get_data()
				min_pos = i
				must_swap = True
			iter = iter.get_next()
			i = i + 1
		while must_swap:
			curr_node_value = curr_node.get_data()
			curr_node.set_data(min_value)
			iter = curr_node.get_next()
			k = curr_pos + 1
			while k < min_pos:
				iter = iter.get_next()
				k = k + 1
			iter.set_data(curr_node_value)
			must_swap = False
		curr_node = curr_node.get_next()
	return linked_list

def find_nth_last_element(linked_list, n):
	num_nodes = size(linked_list)
	if num_nodes == 0:
		return
	if num_nodes == n:
		return linked_list.get_head()
	iter = linked_list.get_head()
	nodes_to_traverse = num_nodes - n
	i = 0
	while i < nodes_to_traverse and iter is not None:
		iter = iter.get_next()
		i = i + 1
	return iter

def add_linked_list(list_a, list_b):
	if size(list_a) == 0 and size(list_b) == 0:
		return
	elif size(list_a) == 0:
		return list_b
	elif size(list_b) == 0:
		return list_a
	else:
		num_nodes_a = size(list_a)
		num_nodes_b = size(list_b)
		iterateA, iterateB = False, False
		if num_nodes_a >= num_nodes_b:
			iterateA = True
		else:
			iterateB = True
		iter_a = list_a.get_head()
		iter_b = list_b.get_head()
		result = linked_list()
		carry_over = 0
		while iterateA and iter_a is not None:
			if iter_b is None:
				if size(result) == 0:
					result.set_head(iter_a)
				else:
					result.add_node_to_tail(iter_a)
				iterateA = False
			else:
				sum = iter_b.get_data() + iter_a.get_data() + carry_over
				if sum > 9:
					carry_over = 1
				else:
					carry_over = 0
				sum_node = node(sum % 10)
				if size(result) == 0:
					result.set_head(sum_node)
				else:
					result.add_node_to_tail(sum_node)
				iter_a = iter_a.get_next()
		return result
