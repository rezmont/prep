from collections import deque

class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, arg):
        super(TreeNode, self).__init__()
        self.val = arg
        self.lock = False
        self.l = None
        self.r = None

    def extend_left(self, arg):
        n = TreeNode(arg)
        self.l = n

    def extend_right(self, arg):
        n = TreeNode(arg)
        self.r = n

    def add_left(self, arg):
        self.l = arg

    def add_right(self, arg):
        self.r = arg

    def __repr__(self):
        left = self.l.val if self.l else 'x'
        right = self.r.val if self.r else 'x'
        return '{1} <- {0}({3}) -> {2}'.format(self.val, left, right, self.lock)

def print_tree(head):
    q = deque([(0, head)])
    while len(q)>0:
        l, ptr = q.popleft()
        if ptr is not None:
            print l, ':', ptr
            q.append((l+1, ptr.l))
            q.append((l+1, ptr.r))


def insert(head, node):
    if head is None or node is None:
        return
    else:
        ptr = head
        last = ptr
        while ptr is not None:
            if node.val == ptr.val :
                return
            last = ptr
            if node.val < ptr.val :
                ptr = ptr.l
            else:
                ptr = ptr.r

        if node.val < last.val:
            last.add_left(node)
        else:
            last.add_right(node)


def delete(head, val):
    if head is None:
        return
    else:
        ptr = head
        last_ptr = ptr
        while ptr is not None:
            if val == ptr.val: 
                if ptr.r is not None:
                    succ_par = ptr
                    succ = ptr.r
                    while succ.l is not None:
                        succ_par = succ
                        succ = succ.l                
                if succ is not None:  # succ found, succ is the parent of succ
                    if succ_par == None:

                    ptr.val = succ.l.val
                    succ.l = succ.l.r
                    return head
                # else:  # no succ
                #     if last_ptr.val == val:  # head removed
                #         head = last_ptr.r
                #         return head
                #     if last_ptr.l is not None and val == last_ptr.l.val:
                #         last_ptr.add_left(ptr.l)
                #         return head
                #     elif last_ptr.r is not None and val == last_ptr.r.val:
                #         last_ptr.add_right(ptr.l)
                #         return head
                #     else:
                #         print 'what'

            last_ptr = ptr
            if val < ptr.val :
                ptr = ptr.l
            else:
                ptr = ptr.r

        if val < last_ptr.val:
            last_ptr.add_left(node)
        else:
            last_ptr.add_right(node)



if __name__ == '__main__':
    arr = [-1*i for i in xrange(10)]

    head = TreeNode(arr[0])
    for i in arr:
        n = TreeNode(i)
        insert(head, n)
    print_tree(head)
    print
    head = delete(head, -9)
    print_tree(head)
