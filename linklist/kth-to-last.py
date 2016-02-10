import random

class NodeSLL(object):
    """docstring for NodeSLL"""
    __slots__ = ['val', 'next']
    def __init__(self, arg):
        super(NodeSLL, self).__init__()
        self.val = arg
        self.next = None

    def set_next(self, n):
        self.next = n

    def __repr__(self):
        vals = [str(self.val)]
        ptr = self.next
        while ptr is not None:
            vals.append(str(ptr.val))
            ptr = ptr.next 
        return ' => '.join(vals)

    def kth_to_last(self, k):
        # ptr_vec = [None for i in xrange(k)]
        ptr_vec = []
        
        for i in xrange(k):
            for j in xrange(i):
                ptr_vec[j] = ptr_vec[j].next
            # ptr_vec[i] = self
            ptr_vec.append(self)
        print len(ptr_vec)
        while ptr_vec[0].next is not None:
            # print ptr_vec[0].val, ptr_vec[-1].val
            for i in xrange(len(ptr_vec)):
                ptr_vec[i] = ptr_vec[i].next
        return ptr_vec[-1]

if __name__ == '__main__':
    tail = None
    for i in xrange(15):
        val = random.randint(0, 10)
        new_node = NodeSLL(val)
        if i == 0:
            head = new_node
        else:
            tail.set_next(new_node)        
        tail = new_node
        
    print head
    k = 5
    x = head.kth_to_last(k)
    print x
    
    # main()