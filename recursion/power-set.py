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

def powerset3(s):
    if len(s)==1:
        return [s, '']        
    
    ret_set = []
    p_set = powerset3(s[1:])
    for el in p_set:
        ret_set.append('{0}, {1}'.format(s[0], el))
        ret_set.append('{0}'.format(el))
    return ret_set


if __name__ == '__main__':
    l = 'abcdedg'
    p_set = powerset2(l)
    # print '\n'.join(p_set)

    p_set = powerset3(l)
    print '\n'.join(p_set)