
def decompose(s, w):
    # print s, w
    global mem
    if len(w)==0:
        if s==0:
            return [[]]
        else:
            return None

    key = '{0},{1}'.format(s, w[0])
    if key in mem:
        lst = mem[key]
        # print 'mem', lst
        return lst

    lst = []
    i = 0
    while i*w[0] <= s:
        # print '>', w[0], i, s
        l = decompose(s - i*w[0], w[1:])
        # print l
        if l is not None:
            # if len(l) == 0:
            #     lst.append(['{0}*{1}'.format(i, w[0])])
            # else:
            for el in l:
                lst.append(el + ['{0}*{1}'.format(i, w[0])])
        i += 1

    mem[key] = lst
    return lst


if __name__ == '__main__':
    mem = {}
    w = [2, 3, 7]
    score = 12
    l = decompose(score, w)
    print l