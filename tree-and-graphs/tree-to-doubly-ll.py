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

    def print_right(self):
        vals = [str(self.val)]
        ptr = self.r
        while ptr is not None:
            vals.append(str(ptr.val))
            ptr = ptr.r 
        return ' => '.join(vals)


    def print_left(self):
        vals = [str(self.val)]
        ptr = self.l
        while ptr is not None:
            vals.append(str(ptr.val))
            ptr = ptr.l 
        return ' => '.join(vals)


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


def BFS(head):
    q = deque()
    q.append(head)
    while len(q)>0:
        node = q.popleft()
        if node is None:
            continue
        q.append(node.l)
        q.append(node.r)
        print node.val


def in_order_covert_to_sorted_doubly(node):
    if node is None:
        return

    global prev_node
    global list_head

    in_order_covert_to_sorted_doubly(node.l)
    
    if list_head is None:
        list_head = node
        print node.val
    if prev_node is not None:
        prev_node.r = node
        node.l = prev_node
    prev_node = node
    
    in_order_covert_to_sorted_doubly(node.r)


if __name__ == '__main__':
    array = range(10)
    head = make_balanced_bst(array)
    print array
    print head

    prev_node = None
    list_head = None
    in_order_covert_to_sorted_doubly(head)



    def print_left(self):
        vals = [str(self.val)]
        ptr = self.r
        while ptr is not None:
            vals.append(str(ptr.val))
            ptr = ptr.r 
        return ' => '.join(vals)

    print list_head.print_right()
    print head.print_left()
