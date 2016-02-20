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

    def x__repr__(self):
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


def inorder2(n):
    q = [n]
    cur = n
    while len(q)>0:
        while cur.l is not None:
            cur = cur.l
            q.append(cur)

        cur = q.pop()
        if cur is not None:
            print cur.val,
        if cur.r is not None:
            cur = cur.r
            q.append(cur)


if __name__ == '__main__':
    arr = [i for i in xrange(10)]
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
    q.clear()
    print head
    preorder(head)
    print
    inorder(head)
    print
    inorder2(head)