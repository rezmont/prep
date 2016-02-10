import random 

def is_all_uniq_chars(sarg):
	visited = set()
	for i in sarg:
		if i in visited:
			return False
		visited.add(i)
	return True 

if __name__ == '__main__':
	s = ''.join([chr(random.randint(97,122)) for _ in xrange(10)])
	# s = ','.join([str(random.randint(0,10)) for _ in xrange(100)])
	print s
	print is_all_uniq_chars(s)
