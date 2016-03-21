


def intersect_sorted(a, b):
    if len(a) == 0 or len(b) == 0:
        return []
    l = []
    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(a) and ptr2 < len(b):
        if a[ptr1] == b[ptr2]:
            l.append(a[ptr1])
            ptr1 += 1
            ptr2 += 1
        elif a[ptr1] < b[ptr2]:
            ptr1 += 1
        else:
            ptr2 += 1
    return l

if __name__ == '__main__':
    a = [i for i in xrange(10)]
    b = [i for i in xrange(2, 20, 2)] 
    c = intersect_sorted(a, b)
    print a
    print b
    print c