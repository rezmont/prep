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

def add_list_digit_wise(head1, head2):
    head = None

    ptr1 = head1
    ptr2 = head2
    carry = 0
    while ptr1 is not None and ptr2 is not None:
        partial_val = ptr1.val+ptr2.val+carry
        if partial_val > 10:
            carry = 1
            partial_val -= 10
        else:
            carry = 0

        if head == None:
            head = NodeSLL(partial_val)
            tail = head
        else:
            tail = tail.add_node(partial_val)

        ptr1 = ptr1.next
        ptr2 = ptr2.next

    while ptr1 is not None:
        partial_val = ptr1.val+carry
        if partial_val > 10:
            carry = 1
            partial_val -= 10
        else:
            carry = 0

        if head == None:
            head = NodeSLL(partial_val)
            tail = head
        else:
            tail = tail.add_node(partial_val)
        ptr1 = ptr1.next

    while ptr2 is not None:
        partial_val = ptr2.val+carry
        if partial_val > 10:
            carry = 1
            partial_val -= 10
        else:
            carry = 0

        if head == None:
            head = NodeSLL(partial_val)
            tail = head
        else:
            tail = tail.add_node(partial_val)
        ptr2 = ptr2.next

    if carry>1:
        tail = tail.add_node(carry)

    return head

def swap(pre_ptr1, ptr1, pre_ptr2, ptr2):
    pre_ptr1.next = pre_ptr2.next
        

if __name__ == '__main__':
    # head = NodeSLL(0)
    # tail = head
    # for i in xrange(15):
    #     tail = tail.add_node(random.randint(0, 10))
    
    digits1 = '4324543'
    head1 = None
    for i in digits1[::-1]:
        if head1 is None:
            head1 = NodeSLL(int(i))
            tail = head1
        else:
            tail = tail.add_node(int(i))
    
    digits2 = '323'
    head2 = None
    for i in digits2[::-1]:
        if head2 is None:
            head2 = NodeSLL(int(i))
            tail = head2
        else:
            tail = tail.add_node(int(i))
    
    print int(digits1)+int(digits2)
    print head1, head2
    head = add_list_digit_wise(head1, head2)
    print head
    