from collections import deque

class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, arg):
        super(TreeNode, self).__init__()
        self.val = arg
        self.l = None
        self.r = None
    
    def add_left(self, n):
        child = TreeNode(n)
        self.l = child
        return child

    def add_right(self, n):
        child = TreeNode(n)
        self.r = child
        return child

    def __repr__(self):
        ret_strings = []
        ret_buff = []
        q = deque()
        q.append((None, self))
        last_p = None
        while len(q)>0:
            p, node = q.popleft()
            if node.l is not None:
                q.append((node, node.l))
            if node.r is not None:
                q.append((node, node.r))

            if p != last_p:
                ret_strings.append(';'.join(ret_buff))
                ret_buff = []
                last_p = p

                parrent = 'None'
                if p is not None:
                    parrent = p.val
                # print parrent, node.val
                ret_buff.append('{0} -> {1}'.format(parrent, node.val))
            else:
                parrent = 'Root'
                if p is not None:
                    parrent = p.val
                # print parrent, node.val
                ret_buff.append('{0} -> {1}'.format(parrent, node.val))
        if len(ret_buff):
            ret_strings.append(';'.join(ret_buff))
        return('\n'.join(ret_strings))

def make_balanced_tree(arr):
    if len(arr) == 0:
        return None

    head = TreeNode(arr[0])
    q = deque()
    q.append(head)
    for i in xrange(1, len(arr), 2):
        node = q.popleft()
        node.add_left(arr[i])
        q.append(node.l)
        
        if len(arr) > (i+1):
            node.add_right(arr[i+1])
            q.append(node.r)
    q.clear()
    return head

def make_balanced_bst(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return TreeNode(arr[0])
    elif len(arr) == 2:
        head = TreeNode(arr[1])
        head.add_left(arr[0])
        return head

    mid = len(arr)/2
    head = TreeNode(arr[mid])
    l = make_balanced_bst(arr[:mid])
    r = make_balanced_bst(arr[mid+1:])
    head.l = l
    head.r = r
    return head


def is_equal(head1, head2):
    s1 = [head1]
    s2 = [head2]
    while len(s1)>0 and len(s2)>0:
        ptr1 = s1.pop()
        ptr2 = s2.pop()
        if ptr1 is None and ptr2 is None:
            continue
        elif (ptr1 is None) ^ (ptr2 is None):
            return False
        if ptr1.val != ptr2.val:
            return False
        s1.append(ptr1.l)
        s1.append(ptr1.r)
        s2.append(ptr2.l)
        s2.append(ptr2.r)

    if len(s1)>0 or len(s2)>0:
        return False
    return True



def is_subtree(head1, head2):
    s = deque()
    s.append(head1)
    while len(s)>0:
        ptr = s.popleft()
        if is_equal(ptr, head2):
            return True
        if ptr.l is not None:
            s.append(ptr.l)
        if ptr.r is not None:
            s.append(ptr.r)

    return False

if __name__ == '__main__':
    arr = range(10)
    head1 = make_balanced_tree(arr)
    print head1
    print    
    arr = [4, 9]
    head2 = make_balanced_tree(arr)
    print head2
    print
    print is_subtree(head1, head2)