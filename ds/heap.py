import random 
from heapq import *

h = []

heappush(h, (1, 'k'))
heappush(h, (4, 'l'))
heappush(h, (4, 'k'))
heappush(h, (10, 'k'))

print h

print heappop(h)
print heappop(h)

print h


x = [random.randint(0,100) for _ in xrange(20)]
print x
heapify(x)
print x