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


def search_for_path(head, path, a):
    if head is None:
        return None
    if head.val == a:
        return '{0}, {1}'.format(path, head.val)
    path = '{0}, {1}'.format(path, head.val)
    ret_val = search_for_path(head.l, path, a)
    if ret_val != None:
        return ret_val
    ret_val = search_for_path(head.r, path, a)
    if ret_val != None:
        return ret_val
    return None

def covers(head, a):
    if head is None:
        return False
    if head.val == a:
        return True
    ret_val = covers(head.l, a)
    if ret_val != False:
        return ret_val
    ret_val = covers(head.r, a)
    if ret_val != False:
        return ret_val
    return False


def first_common_wo_additional_ds(head, a, b):
    if head is None:
        return False

    l_cover = first_common_wo_additional_ds(head.l, a, b)
    r_cover = first_common_wo_additional_ds(head.r, a, b)

    # print head.val
    # print l_cover, r_cover
    
    if (l_cover == a or head.val == a) and (r_cover == b or head.val == b):
        return 'N[{0}]'.format(head.val)
    if (l_cover == b or head.val == b) and (r_cover == a or head.val == a):
        return 'N[{0}]'.format(head.val)

    if l_cover != False:
        return l_cover
    if r_cover != False:
        return r_cover
    
    if l_cover == False and head.val in {a, b}:
        return head.val
    if r_cover == False and head.val in {a, b}:
        return head.val

    return False


def first_common_with_additional_ds(head, a, b):
    p1 = search_for_path(head, '*', a)
    p2 = search_for_path(head, '*', b)
    print p1
    print p2
    


if __name__ == '__main__':
    array = range(10)
    head = make_balanced_tree(array)
    print head
    print
    print first_common_wo_additional_ds(head, 6, 5)