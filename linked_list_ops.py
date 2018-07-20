def size(linked_list):
	head = linked_list.get_head()
	if head is None:
		return 0
	i = 1
	while head.get_next() is not None:
		i = i + 1
		head = head.get_next()
	return i

def print_list(linked_list):
	head = linked_list.get_head()
	while head is not None:
		print(head.get_data(), end= " ")
		head = head.get_next()
	print("")

def insertion_sort_linked_list(linked_list):
	if size(linked_list) == 0:
		return linked_list
	curr_node = linked_list.get_head()
	min_value_pos = 0
	while curr_node.get_next() is not None:
		print_list(linked_list)
		min_value_pos = min_value_pos + 1
		min_value = curr_node.get_data()
		iter = curr_node.get_next()
		i = 0
		while iter is not None:
			if iter.get_data() < min_value:
				min_value = iter.get_data()
				min_value_pos = i
			i = i + 1
			if iter.get_next() is None:
				break
			iter = iter.get_next()
		curr_node_value = curr_node.get_data()
		curr_node.set_data(min_value)
		iter = curr_node.get_next()
		k = 0
		while k < min_value_pos and iter.get_next() is not None:
			iter = iter.get_next()
			k = k + 1
		iter.set_data(curr_node_value)
		curr_node = curr_node.get_next()
	return linked_list
