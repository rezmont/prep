class MyQueue(object):
    """docstring for MyQueue"""
    def __init__(self):
        super(MyQueue, self).__init__()
        # self.arg = arg
        self.__stacks = [[] for _ in xrange(2)]
        self.__mode = 0
    
    def push_back(self, a):
        self.__stacks[self.__mode].append(a)

    def pop_front(self):
        if len(self.__stacks[1 - self.__mode]) == 0:
            while len(self.__stacks[self.__mode]):
                x = self.__stacks[self.__mode].pop()
                self.__stacks[1 - self.__mode].append(x)

        return self.__stacks[1 - self.__mode].pop()

    def __repr__(self):
        return '\n'.join([str(el) for el in self.__stacks])

if __name__ == '__main__':
    q = MyQueue()
    q.push_back(1)
    q.push_back(2)
    q.push_back(3)
    q.push_back(4)
    print q
    print q.pop_front()
    print q
    print 
    q.push_back(5)
    q.push_back(6)
    q.push_back(7)
    print q     
    print q.pop_front()
    
    print q