def perms(string):
    if len(string) == 1:
        return [string]

    l = []
    # for i in xrange(len(string)):
    i = 0
    el = string[i]
    rem = string[:i] + string[i+1:]
    inner_l = perms(rem)
    for item in inner_l:
        for pos in xrange(len(item)+1):
            l.append(item[:pos]+el+item[pos:])
    return l

def perms_no_recursion(string):
    n = len(string)
    m = 1
    for i in xrange(1, n+1):
        m = m*i
    print m
    for i in xrange(m):
        rem = string
        s = []
        p = i
        for j in xrange(n, 0, -1):
            item = p % j
            s.append(rem[item])
            rem = rem[:item] + rem[item+1:]
            p = p / j
        print s


if __name__ == '__main__':
    string = 'abcde'
    print len(perms(string))

    string = 'abc'
    print perms(string)