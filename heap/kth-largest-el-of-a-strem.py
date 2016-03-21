import heapq
import random

def stream():
    for _ in xrange(100):
        yield random.randint(1, 100)


class KthLargest(object):
    """docstring for KthLargest"""
    def __init__(self, arg):
        super(KthLargest, self).__init__()
        self.k = arg
        self.h = []

    def insert(self, arg):
        heapq.heappush(self.h, -1 * arg)
        if len(self.h) > (2*self.k):
            # print self.h
            self.h = sorted(self.h)[:self.k]
            # print self.h
            

    def find_kth_largest(self):
        if len(self.h) < self.k:
            return 'None'
        tmp = sorted(self.h)
        return -1 * tmp[self.k-1]


class KthLargest2(object):
    """docstring for KthLargest"""
    def __init__(self, arg):
        self.k = arg
        self.h = []

    def insert(self, arg):
        if len(self.h) < self.k:
            heapq.heappush(self.h, arg) 
        if self.h[0] < arg:
            heapq.heapreplace(self.h, arg)            

    def find_kth_largest(self):
        if len(self.h) < self.k:
            return 'None'
        return self.h[0]


if __name__ == '__main__':
    s = stream()
    h = KthLargest2(10)
    for i in s:
        h.insert(i)
        print i, h.find_kth_largest()
        # raw_input('...')