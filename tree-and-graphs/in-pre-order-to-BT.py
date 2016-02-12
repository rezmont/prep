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

def build_tree_from_in_pre(in_order, pre_order):
    if len(in_order) == 0:
        return None
    root_val = pre_order[0]
    l_in_order = []
    r_in_order = []
    is_root_met = False
    for el in in_order:
        if el == root_val:
            is_root_met = True
            continue
        if not is_root_met:
            l_in_order.append(el)
        else:
            r_in_order.append(el)

    root = TreeNode(root_val)
    print l_in_order, pre_order[1:len(l_in_order)+1]
    print r_in_order, pre_order[len(l_in_order)+1:]

    l = build_tree_from_in_pre(l_in_order, pre_order[1:len(l_in_order)+1])
    r = build_tree_from_in_pre(r_in_order, pre_order[len(l_in_order)+1:])
    root.l = l
    root.r = r
    return root

if __name__ == '__main__':
    in_order = ['D', 'B' ,'E', 'A', 'F', 'C']
    pre_order = ['A', 'B', 'D', 'E', 'C', 'F']

    # pre_pos_begin = 0
    # pre_pos_end = len(pre_order-1)
    root = build_tree_from_in_pre(in_order, pre_order)
    print root