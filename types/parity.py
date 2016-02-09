import random
import time

def check1():
	a = random.randint(1, 999999)
	cnt = 0
	while a > 0:
		b = a & 0x1
		a = a >> 1
		if b == 1:
			cnt += 1 
	return cnt

def check2():
	a = random.randint(1, 999999)
	return bin(a).count('1')	

if __name__ == '__main__':
	t0 = time.time()
	for i in xrange(10000):
		check1()
	t1 = time.time()
	print t1 - t0
	
	t0 = time.time()
	for i in xrange(10000):
		check2()
	t1 = time.time()
	print t1 - t0
	