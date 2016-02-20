from collections import deque

def tail(filename, n=10):
    'Return the last n lines of a file'
    return deque(open(filename), n)

def tail_list(l, n=10):
    return deque(l, n)


if __name__ == '__main__':
    # print tail('tail-n.py',3)
    print tail_list('dsaddsfsadfdsafsa', 3)