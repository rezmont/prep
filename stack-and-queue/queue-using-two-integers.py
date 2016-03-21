class MiniQueue(object):

    """docstring for MiniQueue"""
    def __init__(self, arg):
        super(MiniQueue, self).__init__()
        self.arg1 = 0
        self.arg1 = 0
        


def find_most_sig(num):
    i = num
    c = 0
    while i > 10:
        i = i / 10
        c += 1
    rem = num - i * (10 ** c)
    return i, rem

if __name__ == '__main__':
    a, b = find_most_sig(4323451)
    print a, b