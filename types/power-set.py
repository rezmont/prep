import random
from itertools import chain, combinations

def powerset1(iterable):
    s = list(iterable)
    print list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))


def powerset2(iterable):
    s = list(iterable)
    p = 2 ** len(s)
    for i in xrange(p):
        b = bin(i)
        b = b[2:]
        b = '{0}{1}'.format('0'*(len(s)-len(b)), b)
        # print b
        lst = []
        for j, el in enumerate(b):
            if el=='1':
                lst.append(s[j])
        print lst



if __name__ == '__main__':
    # rand_set = set()
    # for i in xrange(10):
    #     rand_set.add(i)
    # powerset2(rand_set)

    rand_lst = []
    for i in xrange(10):
        rand_lst.append(i)
    powerset1(rand_lst)
    
