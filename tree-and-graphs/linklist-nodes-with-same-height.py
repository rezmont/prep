from collections import deque
import sys

class SLLNode(object):
    def __init__(self, arg):
        self.obj_ptr = arg
        self.next = None

    def add_next(self, arg):
        self.next = arg

    def __repr__(self):
        str_arr = []
        ptr = self
        while ptr is not None:
            str_arr.append(str(ptr.obj_ptr.val))
            ptr = ptr.next
        return ' -> '.join(str_arr)


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

def link_same_height_nodes(head):
    ptr_list_head = []
    ptr_list_tail = []
    q = deque()
    q.append((0, head))
    while len(q)>0:
        h, node = q.popleft()
        if h >= len(ptr_list_head):
            aux_head = SLLNode(node)
            ptr_list_head.append(aux_head)
            ptr_list_tail.append(aux_head)
        else:
            ptr_list_tail[h].add_next(SLLNode(node))
            ptr_list_tail[h] = ptr_list_tail[h].next

        if node.l is not None:
            q.append((h+1, node.l))
        if node.r is not None:
            q.append((h+1, node.r))

    return ptr_list_head

if __name__ == '__main__':
    array = range(10)
    head = make_balanced_tree(array)

    ptrs = link_same_height_nodes(head)    
    print array
    print head
    print
    print ptrs[2]
