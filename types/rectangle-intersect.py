import random

def make_rect():
	base = (random.randint(0, 10), random.randint(0, 10))
	return [base, (base[0]+random.randint(0, 10), base[1]+random.randint(0, 10))]

def check_overlap(r1, r2):
	x = r1[0][0] < r2[1][0] and r2[0][0] < r1[1][0]
	y = r1[0][1] < r2[1][1] and r2[0][1] < r1[1][1]
	print x and y


if __name__ == '__main__':
	r1 = make_rect()
	r2 = make_rect()
	print r1, r2
	check_overlap(r1, r2)