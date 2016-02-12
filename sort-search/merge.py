def merge(l, s):
    len_s = len(s)
    len_l = len(l) - len_s
    
    for i in xrange(len_l-1, -1, -1):
        l[i+len_s] = l[i]
        # l[i] = 0
    print l

    ptr_l = len_s
    ptr_s = 0
    ptr_w = 0
    while ptr_l < len_s+len_l and ptr_s < len_s:
        print l[ptr_l], s[ptr_s]
        if l[ptr_l] <= s[ptr_s]:
            l[ptr_w] = l[ptr_l]
            ptr_l += 1
            ptr_w += 1
        else:
            l[ptr_w] = s[ptr_s]
            ptr_s += 1
            ptr_w += 1

    while ptr_s < len_s:
        l[ptr_w] = s[ptr_s]
        ptr_s += 1
        ptr_w += 1

    return l


if __name__ == '__main__':
    a = [i for i in xrange(0,20,2)]
    a.extend([0 for _ in xrange(5)])

    b = [i for i in xrange(1,11,2)]

    print a
    print b
    print merge(a, b)