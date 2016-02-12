import random

def anagram_comp(s1, s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    return s1 < s2


def anagram(s1):
    s1 = ''.join(sorted(s1))
    return s1



if __name__ == '__main__':
    l = [''.join([chr(random.randint(97,100)) for _ in xrange(5)]) for _ in xrange(20)]
    print l
    print sorted(l, key=anagram)
    print sorted(l, cmp=anagram_comp)