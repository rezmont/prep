import collections
import random
import sys

if __name__ == '__main__':
    # print collections.Counter('2321321321')
    l = [
        collections.Counter([chr(random.randint(97, 102)) for _ in xrange(20)])
        for _ in xrange(10)
    ]
    print l
    l = collections.Counter([chr(random.randint(97, 102)) for _ in xrange(20)])
    print l
    print l['x']