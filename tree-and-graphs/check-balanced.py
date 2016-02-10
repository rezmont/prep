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

    def is_balanced(self):
        q = deque()
        q.append((0, self))
        min_height = sys.maxint
        max_height = 0
        while len(q)>0:
            h, node = q.popleft()
            is_leaf = True
            if node.l is not None:
                is_leaf = False
                q.append((h+1, node.l))
            if node.r is not None:
                is_leaf = False
                q.append((h+1, node.r))
            if is_leaf:
                if h > max_height:
                    max_height = h
                if h < min_height:
                    min_height = h

            if min_height != sys.maxint and max_height != 0:
                if max_height - min_height >= 2:
                    return False
        return True        

if __name__ == '__main__':
    root = TreeNode(0)
    l = root.add_left(1)
    r = root.add_right(2)
    ll = l.add_left(3)
    lll = ll.add_left(4)
    print root
    print root.is_balanced()