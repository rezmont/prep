from collections import deque

class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, arg):
        super(TreeNode, self).__init__()
        self.val = arg
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
        return '{1} <- {0} -> {2}'.format(self.val, left, right)

def is_symmetric(head):
    if head == None:
        return True
    s1 = [head.l]
    s2 = [head.r]
    while len(s1) > 0 and len(s2) > 0:
        ptr1 = s1.pop()
        ptr2 = s2.pop()

        if ptr1 is None and ptr2 is not None:
            return False
        if ptr1 is not None and ptr2 is None:
            return False
        if ptr1 is not None and ptr2 is not None:
            if ptr1.val != ptr2.val:
                print ptr1, ptr2
                return False
            s1.append(ptr1.l)
            s2.append(ptr2.r)

            s1.append(ptr1.r)
            s2.append(ptr2.l)
    if len(s1) > 0 or len(s2) > 0:
        return False
    else:
        return True 

def print_tree(head):
    q = deque([(0, head)])
    while len(q)>0:
        l, ptr = q.popleft()
        if ptr is not None:
            print l, ':', ptr
            q.append((l+1, ptr.l))
            q.append((l+1, ptr.r))

def make_btree(arr):
    head = TreeNode(arr[0])
    q = deque([head])
    i = 1
    while i < len(arr):
        ptr = q.popleft()

        node = TreeNode(arr[i]) 
        ptr.add_left(node)
        q.append(node)
        i += 1
        if i >= len(arr):
            break
        node = TreeNode(arr[i])
        ptr.add_right(node)
        q.append(node)
        i += 1
    return head

def make_btree_aux(arr):
    head = TreeNode(arr[0])
    q = deque([head])
    i = 1
    while i < len(arr):
        ptr = q.popleft()

        node = TreeNode(arr[i]) 
        ptr.add_right(node)
        q.append(node)
        i += 1
        if i >= len(arr):
            break
        node = TreeNode(arr[i])
        ptr.add_left(node)
        q.append(node)
        i += 1
    return head

if __name__ == '__main__':
    arr = [i for i in xrange(5)]
    # print_tree(head)
    left = make_btree(arr)
    right = make_btree(arr)
    
    head  = TreeNode(-1)
    head.add_left(left)
    head.add_right(right)
    print_tree(head)
    ret = is_symmetric(head)
    print ret