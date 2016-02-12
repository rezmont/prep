import math

def all_permutations_non_recursive(s):
    f = math.factorial(len(s))
    perms = []
    for i in xrange(f):
        partial = s
        rem = i
        vec = []
        for j in xrange(len(s), 1,-1):
            # print rem % j,
            index = rem % j
            rem /= j 
            vec.append(partial[index])
            partial = partial[:index] + partial[index+1:]
        vec.append(partial)
        print ''.join(vec)
        perms.append(''.join(vec))
    print len(set(perms))


def all_permutations(s):
    if len(s)==1:
        return [s]

    ret_l = []
    for i, c in enumerate(s):
        # print i, s, s[:i], 
        remainder = '{0}{1}'.format(s[:i], s[i+1:])
        tmp_l = all_permutations(remainder)
        for el in tmp_l:
            ret_l.append('{0}{1}'.format(c, el))
    return ret_l


if __name__ == '__main__':
    s = 'abcde'
    # perm_l = all_permutations(s)
    # print '\n'.join(perm_l)

    perm_l = all_permutations_non_recursive(s)
    # print '\n'.join(perm_l)