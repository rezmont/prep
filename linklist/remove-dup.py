import random

class NodeSLL(object):
    """docstring for NodeSLL"""
    def __init__(self, arg):
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

    def remove_duplicate(self):
        seen = set([self.val])
        ptr_last_not_seen = self
        ptr = self.next
        while ptr is not None:
            if ptr.val in seen:
                ptr_last_not_seen.next = ptr.next
            else:
                ptr_last_not_seen = ptr
            seen.add(ptr.val)
            ptr = ptr.next 


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
    head.remove_duplicate()
    print head
    
    # main()