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

def preorder_marker(head):
    if head is None:
        print 'x',
        return
    print head.val,
    preorder_marker(head.l)
    preorder_marker(head.r)
    
def __construct_from_preorder_marked(l):
    if l[0] == 'x':
        return None

    head = TreeNode(l[0])
    left, rem = construct_from_preorder_marked(l[1:0])
    last = head
    add_left = True
    i = 1
    while i < len(l):
        if l[i] != 'x':
            n = TreeNode(l[i])
            stack[-1].add_left(n)
        else:
            pass

def construct_from_preorder_marked(l):
    if len(l) == 0:
        return None

    head = TreeNode(l[0])
    last = head
    stack = [(head, 'r'), (head, 'l')]
    i = 1
    while i < len(l):
        if len(s) == 0:
            return False
        if l[i] != 'x':
            n = TreeNode(l[i])
            ptr, d = stack.pop()
            if d == 'l':
                ptr.add_left(n)
            else:
                ptr.add_right(n)
            stack.append((n, 'r'))
            stack.append((n, 'l'))
        else:
            ptr, d = stack.pop()
        i += 1
    return head



if __name__ == '__main__':
    # arr = [i for i in xrange(10)]
    # head = make_btree(arr)
    # print_tree(head)
    # preorder_marker(head)
    # print
    # s = '0 1 3 7 x x 8 x x 4 9 x x x 2 5 x x 6 x x'
    # l = s.split(' ')
    # h2 = construct_from_preorder_marked(l)
    # print_tree(h2)


    head = TreeNode(0)
    head.extend_right(1)
    head.r.extend_right(2)
    head.r.r.extend_right(3)
    print_tree(head)
    preorder_marker(head)
    print
    s = '0 x 1 x 2 x 3 x x'
    l = s.split(' ')
    h2 = construct_from_preorder_marked(l)
    print_tree(h2)
