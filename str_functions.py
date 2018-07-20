def replace(s,c,r):
	result = []
	for ch in s:
		if ch == c:
			result.append(r)
		else:
			result.append(ch)
	result = "".join(result)
	return result

def replace_in_place(s,c,r):
	i = 0
	ns = len(s)
	nr = len(r)
	while i < ns:
		if s[i] == c:
			temp = s[i+1:]
			nt = len(temp)
			for j in range(nr):
				# wont work! String doesn't support assignment operation in python
				s[i+j] = r[j]
			for k in range(nt):
				# wont work!
				s[i+k+nr] = temp[k]
		i+=1
	return s	
		
def recursive_replace(s,c,r):
	if len(s) == 0:
		return s
	elif s == c:
		return r
	else:
		if s[0] == c:
			return r + replace_recursive(s[1:],c,r)
		else:
			return s[0] + replace_recursive(s[1:],c,r)

def reverse(s):
	result = []
	i = len(s) - 1
	while i >= 0:
		result.append(s[i])
		i = i - 1
	result = "".join(result)
	return result

def recursive_reverse(s):
	if len(s) == 0:
		return s
	else:
		return s[-1] + recursive_reverse(s[:-1])
	
def anagram(s1, s2):
	if len(s1) != len(s2):
		return False 
	ns = len(s1)
	j = ns - 1
	for i in range(ns):
		if s1[i] != s2[j]:
			return False
		j = j - 1
	return True

def recursive_anagram(s1,s2):
	if len(s1) != len(s2):
		return False
	if len(s1) == 0:
		return True
	else:
		if s1[0] == s2[-1]:
			return recursive_anagram(s1[1:], s2[:-1])
		else:
			return False

def set_zero(m):
	if len(m) == 0:
		return m
	nm = len(m)
	nn = len(m[0])
	i = 0 
	while i < nm: 
		zero = -1
		j = 0
		while j < nn:
			if m[i][j] == 0:
				zero = j
			j = j + 1
		k = 0
		while k < nn and zero != -1:
			m[i][k] = 0
			k = k + 1
		if zero != -1:
			l = 0
			while l < nm:
				m[l][zero] = 0
				l = l + 1
		i = i + 1
	return m