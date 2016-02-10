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

def partition_around(head, n):
    head1, tail1 = None, None
    head2, tail2 = None, None
    ptr = head
    while ptr is not None:
        if ptr.val < n:
            if head1 is None:
                head1 = ptr
                tail1 = ptr
            else:
                tail1.next = ptr
                tail1 = ptr
        else:
            if head2 is None:
                head2 = ptr
                tail2 = ptr
            else:
                tail2.next = ptr
                tail2 = ptr
        ptr = ptr.next

    if head1 is not None and head2 is not None:
        tail1.next = head2
        return head1
    elif head1 is not None:
        return head1
    else:
        return head2

def swap(pre_ptr1, ptr1, pre_ptr2, ptr2):
    pre_ptr1.next = pre_ptr2.next
        

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
    x = partition_around(head, 1)
    print x
    
    # main()