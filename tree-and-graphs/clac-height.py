class TreeNode(object):
    def __init__(self, v):
        self.val = v
        self.kids = []
    
    def push_kid(self, v):
        self.kids.append(v)

    def add_kid(self, v):
        t = TreeNode(v)
        self.kids.append(t)
    
    def __str__(self):
        s = '{}: '.format(self.val)
        for el in self.kids:
            s += str(el.val) + ','

        l = [s]
        for el in self.kids:
            l.append(str(el))
        return '\n'.join(l)

    def __repr__(self):
        l = '{}'.format(self.val)
        return l 

def clac_height(n):
    h = 0
    for k in n.kids:
        t = clac_height(k)
        h = t if t > h else h 
    return h+1

if __name__ == '__main__':
    head = TreeNode(0)
    for i in xrange(1, 4):
        head.add_kid(i)

    for i in xrange(2):
        for j in xrange(2):
            head.kids[i].add_kid((i+1)*10+j)
    head.kids[0].kids[0].add_kid(100)
    head.kids[0].kids[0].kids[0].add_kid(1000)

    print head
    print 'heigh:', clac_height(head)