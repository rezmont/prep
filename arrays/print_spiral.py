def trans(pos, l):
    inward = 0
    while pos >= 4*(l-1) and (l-1)>0:
        pos -= 4*(l-1)
        l -= 2
        inward += 1

    if pos<(l-1):
        x = 0
        y = pos
        return '1', inward+x, inward+y 
    elif pos<2*(l-1):
        x = pos - (l-1)
        y = l-1
        return '2', inward+x, inward+y
    elif pos<3*(l-1):
        x = l-1
        y = l-1 - (pos - 2*(l-1))
        return '3', inward+x, inward+y
    else:
        x = l-1 - (pos - 3*(l-1))
        y = 0
        return '4', inward+x, inward+y


def print_spiral(mat):
    path_len(len(mat)*len(mat))
    for i in xrange(path_len):
        x, y = trans(i, len(mat))
        print mat[x][y]


if __name__ == '__main__':
    l = 3
    for i in xrange(l*l):
        com, x, y = trans(i, l)
        print i, ':', com, x, y
