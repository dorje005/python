def sort_stack(s, result, peg_a, peg_b):
	if s.is_empty() and peg_a.is_empty() and peg_b.is_empty():
		return result
	elif not s.is_empty():
		min = s.find_min()
		item = s.pop()
		if min == item:
			result.push(item)
			print("MIN: ", item, " popped!")
		else:
			peg_a.push(item)
		return sort_stack(s, result, peg_a, peg_b)
	elif not peg_a.is_empty():
		min = peg_a.find_min()
		item = peg_a.pop()
		if min == item:
			result.push(item)
			print("MIN: ", item, " popped!")
		else:
			peg_b.push(item)
		return sort_stack(s, result, peg_a, peg_b)
	elif not peg_b.is_empty():
		min = peg_b.find_min()
		item = peg_b.pop()
		if min == item:
			result.push(item)
			print("MIN: ", item, " popped!")
		else:
			peg_a.push(item)
		return sort_stack(s, result, peg_a, peg_b)
		