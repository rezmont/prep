from collections import deque

class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, arg):
        super(TreeNode, self).__init__()
        self.val = arg
        self.r = None
        self.l = None
    
    def set_left(self, arg):
        self.l = arg

    def set_right(self, arg):
        self.r = arg

def print_bt(head):
    ret_strings = []
    ret_buff = []
    q = deque()
    q.append((None, head))
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
            parrent = 'None'
            if p is not None:
                parrent = p.val
            # print parrent, node.val
            ret_buff.append('{0} -> {1}'.format(parrent, node.val))
    if len(ret_buff):
        ret_strings.append(';'.join(ret_buff))
    print('\n'.join(ret_strings))

def preorder(n):
    q = [n]
    while len(q)>0:
        el = q.pop()
        if el == None:
            print 'x',
        else:
            print el.val,
            q.append(el.r)
            q.append(el.l)


def inorder(n):
    q = [n]
    while len(q)>0:
        el = q.pop()
        if el == None:
            print 'x',
        elif isinstance(el, int):
            print el, 
        else:
            q.append(el.r)
            q.append(el.val)
            q.append(el.l)

def create_smaple_bt(arr):
    print arr
    head = TreeNode(arr[0]) 
    tail = head
    # q = deque()
    q = deque([head])
    i = 1
    while i<len(arr):
        tail = q.popleft()

        nl = TreeNode(arr[i])
        tail.set_left(nl)
        q.append(nl)
        i += 1
        if i==len(arr):
            break
        nr = TreeNode(arr[i])    
        tail.set_right(nr)
        q.append(nr)
        i += 1
    return head

def first_common_ancestor(ptr, a, b):
    if ptr is None:
        return False
    # print
    # print_bt(ptr)
    left = first_common_ancestor(ptr.l, a, b)
    right = first_common_ancestor(ptr.r, a, b)
    print ptr.val, left, right
    if left != False and left != a and left != b:
        return left
    if right != False and right != a and right != b:
        return right

    if left == a and (right == b or ptr.val == b):
        return ptr
    if left == b and (right == a or ptr.val == a):
        return ptr
    
    if left == a:
        if right == b or ptr.val == b:
            return ptr
        if right == False:
            return a
    if left == b:
        if right == a or ptr.val == a:
            return ptr
        if right == False:
            return b
    if left == False:
        if right == False:
            if ptr.val == a and ptr.val == b:
                return ptr
            if ptr.val == a:
                return a
            if ptr.val == b:
                return b
        if right == a and ptr.val == b:
            return ptr
        elif right == a:
            return a
        if right == b and ptr.val == a:
            return ptr
        elif right == b:
            return b
    # print '>> gotten here:', left, right, ptr.val, '<<<'
    return False

if __name__ == '__main__':
    arr = [i for i in xrange(10)]
    head = create_smaple_bt(arr)
    print_bt(head)

    ancestor = first_common_ancestor(head, 1, 9)
    if ancestor== False or isinstance(ancestor, int):
        print ancestor
    else:
        print_bt(ancestor)
