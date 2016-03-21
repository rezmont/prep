def binom(n, k):
    global mem
    if n==k or k==0:
        return 1

    key = '{0},{1}'.format(n, k)
    if key in mem:
        return mem[key]
    m = binom(n-1, k-1) * n / k
    mem[key] = m
    return m

if __name__ == '__main__':
    mem = {}
    v = binom(10, 5)
    print v


