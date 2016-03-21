class CircularQueue(object):
    """docstring for CircularQueue"""
    def __init__(self, max_size):
        super(CircularQueue, self).__init__()
        self.q = [-1 for _ in xrange(max_size)]
        self.cap = max_size
        self.filled = 0
        self.tail = 0
        self.head = 0

    def enque(self, item):
        self.q[self.head] = item 
        self.head = (self.head+1) % self.cap
        if self.filled < self.cap:
            self.filled += 1
        else:
            self.tail = (self.tail+1) % self.cap 
        print 'head:', self.head, '\ttail:', self.tail

    def deque(self):
        if self.filled > 0:
            self.filled -= 1
            item = self.q[self.tail]
            self.tail = (self.tail+1) % self.cap 
            return item
        else:
            return None

    def size(self, max_size):
        self.cap = max_size
        orig_size = len(self.q)
        diff_size = max_size - len(self.q)

        self.q = self.q + [-1 for _ in xrange(diff_size)]
        if self.head < self.tail:
            for i in xrange(head):
                self.q[(orig_size+i)%max_size] = self.q[i]
            self.head = (self.tail + self.filled) % max_size
        return self.filled

    def __repr__(self):
        return str(self.q)
        # print 'head:', self.head, '\ttail:', self.tail

if __name__ == '__main__':
    cq = CircularQueue(3)
    cq.enque(1)
    cq.enque(2)
    cq.enque(3)
    cq.enque(4)
    cq.enque(5)
    print cq
    print cq.deque()
    cq.size(10)
    cq.enque(10)
    cq.enque(20)
    cq.enque(30)
    cq.enque(40)
    print cq.tail
    print cq
    print cq.deque()
    print cq.deque()
    print cq.deque()
    print cq.deque()
    print cq.deque()
    print cq.head
    cq.enque(100)
    print cq
