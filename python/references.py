"""
"""


def aFunction(arr):
    arr[0] = -1
    print 'in function', arr

arr = [i for i in xrange(10)]
aFunction(list(arr))
print 'after function', arr

aFunction(arr[:])
print 'after function', arr



d = {i:i for i in xrange(10)}
aFunction(dict(d))
print 'after function', d

d = {i:i for i in xrange(10)}
aFunction(d.copy())
print 'after function', d