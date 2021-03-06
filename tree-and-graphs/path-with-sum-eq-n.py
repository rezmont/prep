from collections import deque
import sys

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


def find_paths_with_sum_from(head, path, already_sat, total):
    if head is None:
        return    
    path = '{0}->{1}'.format(path, head.val)
    if head.val + already_sat < total:
        find_paths_with_sum_from(head.l, path, head.val + already_sat, total)
        find_paths_with_sum_from(head.r, path, head.val + already_sat, total)
    elif head.val + already_sat == total:
        print path



def find_paths_with_sum(head, total):
    s = [head]
    while len(s)>0:
        ptr = s.pop()
        if ptr is None:
            continue
        find_paths_with_sum_from(ptr, '', 0, total)
        s.append(ptr.l)
        s.append(ptr.r)
        

if __name__ == '__main__':
    array = range(10)
    head = make_balanced_bst(array)
    print array
    print head
    print

    find_paths_with_sum(head, 7)
