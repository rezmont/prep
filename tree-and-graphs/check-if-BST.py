import sys
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
                parrent = 'None'
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

def is_BST(head, min_val=(-sys.maxint - 1), max_val=sys.maxint):
    val = head.val
    is_leaf = True
    if head.l is not None:
        l_bst, l_min, l_max = is_BST(head.l, min_val, val)
        if l_bst == False:
            return False, 0, 0
        is_leaf = False
    if head.r is not None:
        r_bst, r_min, r_max = is_BST(head.r, val+1, max_val)
        if r_bst == False:
            return False, 0, 0
        is_leaf = False
    
    if is_leaf:
        return True, val, val
    else:
        if head.l is None: 
            if val < r_min:
                return True, val, r_max
            else:
                return False, 0, 0
        elif head.r is None:
            if l_max <= val:
                return True, l_min, val
            else:
                return False, 0, 0
        elif l_max <= val and val < r_min:
            return True, l_min, r_max
        else:
            return False, 0, 0


def is_BST2(head, min_val=(-sys.maxint - 1), max_val=sys.maxint):
    if head is None:
        return True
    else:
        print head.val, min_val, max_val
    if head.val > max_val or head.val < min_val:
        return False
    if (not is_BST2(head.r, head.val+1, max_val)) or (not is_BST2(head.l, min_val, head.val)):
        return False
    return True


if __name__ == '__main__':
    arr = range(10)
    # arr[4] = 100
    head = make_balanced_bst(arr)
    # head = make_balanced_tree(arr)
    print is_BST2(head)