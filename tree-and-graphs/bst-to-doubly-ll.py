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
        left = self.l.val if self.l else 'x'
        right = self.r.val if self.r else 'x'
        return '{1} <- {0} -> {2}'.format(self.val, left, right)

    def __repr__aux(self):
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


def print_tree(head):
    q = deque([(0, head)])
    while len(q)>0:
        l, ptr = q.popleft()
        if ptr is not None:
            print l, ':', ptr
            q.append((l+1, ptr.l))
            q.append((l+1, ptr.r))


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


def inorder_doublyll(head):
    stack = [('1', head)]
    pred = None
    first = None
    while len(stack):
        k, v = stack.pop()
        # print k, v
        if v is not None:
            if k == '0':
                if pred is None:
                   first = v 
                   pred = v
                else:
                    pred.r = v
                    v.l = pred
                    pred = v
            else:
                stack.append(('1', v.r))
                stack.append(('0', v))
                stack.append(('1', v.l))
    return first


def inorder_doublyll_2(head):
    print head
    raw_input('...')
    if head is None:
        return None, None 
    
    pred = head.l
    post = head.r
    pred_l, post_l = inorder_doublyll_2(head.l)
    pred_h, post_h = inorder_doublyll_2(head.r)
    if pred_l is not None:
        head.l = post_l
        pred_l.r = head
        pred = pred_l
    if pred_h is not None:
        head.r = pred_h
        pred_h.l = head
        post = post_h 

    return pred, post

if __name__ == '__main__':
    array = range(10)
    head = make_balanced_bst(array)
    print array
    print_tree(head)

    first = inorder_doublyll(head)
    ptr = first
    while ptr is not None:
        print ptr, 
        ptr = ptr.r
    print

    first, last = inorder_doublyll_2(head)
    ptr = first
    while ptr is not None:
        print ptr, 
        ptr = ptr.r