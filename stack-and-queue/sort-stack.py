class DoubleSortedStack(object):
    """docstring for DoubleSortedStack"""
    def __init__(self):
        super(DoubleSortedStack, self).__init__()
        self.stack = []
        self.stack_aux = []

    def push(self, num):
        if len(self.stack) == 0:
            self.stack.append(num)
        elif num > self.stack[-1]:
            self.stack.append(num)
        else:
            while num < self.stack[-1]:
                self.stack_aux.append(self.stack.pop())

            self.stack.append(num)
            while len(self.stack_aux)>0:
                self.stack.append(self.stack_aux.pop())


    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def __repr__(self):
        buff = '\n'.join([str(self.stack), str(self.stack_aux)])
        buff += '\n'
        return buff


if __name__ == '__main__':
    s = DoubleSortedStack()
    a = s.pop()
    print a
    s.push(1)
    s.push(2)
    s.push(10)
    print s
    s.push(7)
    print s
