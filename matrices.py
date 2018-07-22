def set_zero(m):
	if len(m) == 0:
		return m
	num_rows = len(m)
	num_cols = len(m[0])
	i = 0 
	zeros = []
	while i < num_rows: 
		zero_exists = False
		j = 0
		while j < num_cols:
			if m[i][j] == 0:
				zeros.append(j)
				zero_exists = True
			j = j + 1
		k = 0
		while k < num_cols and zero_exists:
			m[i][k] = 0
			k = k + 1
		i = i + 1
	i = 0
	while i < num_rows:
		for j in zeros:
			m[i][j] = 0
		i = i + 1
	
def set_zero(m):
	if len(m) == 0:
		return m
	num_rows = len(m)
	num_cols = len(m[0])
	i = 0 
	zeros = []
	while i < num_rows: 
		zero_exists = False
		j = 0
		while j < num_cols:
			if m[i][j] == 0:
				zeros.append(j)
				zero_exists = True
			j = j + 1
		k = 0
		while k < num_cols and zero_exists:
			m[i][k] = 0
			k = k + 1
		i = i + 1
	i = 0
	while i < num_rows:
		for j in zeros:
			m[i][j] = 0
		i = i + 1
	
	return m