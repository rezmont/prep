def atoi(sarg):
	if len(sarg) == 0:
		return None
	sign = sarg[0]
	if sign == '-' or sign == '+':
		sarg = sarg[1:]
	ret_val = 0
	for i, el in enumerate(sarg):
		el_val = ord(el) - ord('0')
		ret_val = ret_val*10 + el_val
		if el_val > 9 or el_val < 0:
			return None

	if sign == '-':
		return ret_val*-1


if __name__ == '__main__':
	print(atoi('-23432'))