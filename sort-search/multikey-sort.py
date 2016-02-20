import random

if __name__ == '__main__':
    arr = [(random.randint(1,10),(random.randint(1, 10))) for _ in xrange(10)]
    x = sorted(arr, key=(lambda x: (x[1], x[0])))
    print x