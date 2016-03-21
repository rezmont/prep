class trieNode(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
    
    def add_child(self, val):
        if val not in self.children:
            c = trieNode(val)
            self.children[val] = c
            return c
        else:
            return self.children[val]

    def has_child(self, val):
        if val not in self.children:
            return None
        else:
            return self.children[val]
    
    def __str__(self):
        s = '{0} -> {1}'.format(self.val, self.children.keys())  
        return s

class trie(object):
    def __init__(self):
        self.root = trieNode('')
        # print self.root

    def insert(self, s):
        if len(s)>0:
            ptr = self.root
            print type(ptr)

            for el in s:
                print el
                ptr = ptr.add_child(el)
            ptr.add_child('_end_')

    def look_up(self, s):
        if len(s)>0:
            ptr = self.root
            for el in s:
                ptr = el.has_child(s)
                if ptr is None:
                    return None
            return ptr

    def __repr__(self):
        l = []
        s = [self.root]
        while len(s)>0:
            ptr = s.pop()
            l.append(str(ptr))
            for k, v  in ptr.children.iteritems():
                s.append(v)
        return '\n'.join(l)


if __name__ == '__main__':
    t = trie()
    t.insert('brandi')
    print t
    t.insert('reza')
    t.insert('remo')
    print t