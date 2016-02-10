import random


def rearrange(arr, pos):
	el = arr[pos]
	print 'element:', el
	# new_pos =
	# no_eq = 0
	l = 0
	r = len(arr)-1
	print arr
	while l <= r:
		print 'new bounds {0}, {1}'.format(l, r) 
		# l = l
		# r = r
		while arr[l] < el and l<len(arr)-1:
			l += 1
		while arr[r] > el and r>0:
			r -= 1

		if l <= r:
			if arr[l] == el and arr[r] == el:
				mid_pos = -1
				for i in xrange(l+1, r):
					if arr[i] != el:
						mid_pos = i
						break
				if mid_pos == -1:
					print arr
					return
				else:
					if arr[mid_pos] < el:
						arr[l], arr[mid_pos] = arr[mid_pos], arr[l]
						l += 1
					else:
						arr[r], arr[mid_pos] = arr[mid_pos], arr[r]
						r += 1
				print 'mid', l, r, '->', arr[l], arr[r]
				print arr

			else:
				print l, r, '->', arr[l], arr[r]
				arr[l], arr[r] = arr[r], arr[l]
				print arr

				# if arr[l] < el:
				# 	l += 1
				# if arr[r] > el:	
				# 	r -= 1
		raw_input('...')
	print arr


def rearrange2(arr, pos):
	el = arr[pos]

	print 'element:', el
	no_eq = 0
	smaller_ptr = 0
	bigger_ptr = len(arr)-1
	i = 0
	while smaller_ptr+no_eq <= bigger_ptr:
		print 'arr{0}:{1}'.format(i, arr[i]), 'small', smaller_ptr, 'big', bigger_ptr
		if arr[i] < el:
			arr[smaller_ptr] = arr[i]
			smaller_ptr += 1
			i += 1
		elif arr[i] > el:
			a[i], arr[bigger_ptr] = arr[bigger_ptr], a[i]
			bigger_ptr -= 1
		else:
			no_eq += 1
			i+=1
		print arr

	for i in xrange(no_eq):
		arr[i+smaller_ptr] = el
	print
	print arr


if __name__ == '__main__':
	a = [random.randint(0,10) for i in xrange(30)]
	# a = [10, 9, 6, 9, 7, 3, 6, 1, 4, 8, 2, 3, 2, 3, 5, 4, 9, 10, 10, 0, 7, 9, 3, 6, 7, 6, 2, 9, 3, 4]
	rearrange2(a, 0)