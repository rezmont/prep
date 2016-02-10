class HanoiSolver(object):
    """docstring for HanoiSolver"""
    def __init__(self, num):
        super(HanoiSolver, self).__init__()
        self.l = num 
        self.s = [[] for _ in xrange(3)]
        self.s[0] = [num-i for i in xrange(num)]
        self.s[1] = []
        self.s[2] = []

    def __repr__ (self):
        return '{0}\n{1}\n{2}'.format(self.s[0], self.s[1], self.s[2])

    def move(self, n, orig, buff, dest):
        if n == 0:
            return
        
        self.move(n-1, orig, dest, buff)
        
        x = self.s[orig].pop()
        print('moving {0} from {1} to {2}'.format(x, orig, dest))
        self.s[dest].append(x)
        print self
        raw_input('... moved {0} for {1}'.format(x, n))
        
        self.move(n-1, buff, orig, dest)

        print
        print self

        

if __name__ == '__main__':
    n = 4
    hn = HanoiSolver(n)
    print hn
    hn.move(n, 0, 1, 2)