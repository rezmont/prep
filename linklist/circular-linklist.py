import random

class NodeSLL(object):
    """docstring for NodeSLL"""
    __slots__ = ['val', 'next']
    def __init__(self, arg):
        super(NodeSLL, self).__init__()
        self.val = arg
        self.next = None

    def add_node(self, num):
        n = NodeSLL(num)
        self.next = n
        return n

    def set_next(self, n):
        self.next = n

    def __repr__(self):
        vals = [str(self.val)]
        ptr = self.next
        while ptr is not None:
            vals.append(str(ptr.val))
            ptr = ptr.next 
        return ' => '.join(vals)


def find_loop(head):
    d = {}
    ptr = head
    while ptr.next is not None:
        # if id(ptr) is in d:
        if ptr.val in d:
            return ptr.val
        d[ptr.val] = ptr.val
        ptr = ptr.next



def swap(pre_ptr1, ptr1, pre_ptr2, ptr2):
    pre_ptr1.next = pre_ptr2.next
        

if __name__ == '__main__':  
    digits1 = 'abcbdaded'
    head = None
    for i in digits1:
        if head is None:
            head = NodeSLL(i)
            tail = head
        else:
            tail = tail.add_node(i)
        
    print head
    head = find_loop(head)
    print head
    