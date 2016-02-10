import random


class Matrix(object):
    """docstring for Matrix"""
    def __init__(self, n, m, *args):
        mat = [[random.randint(0,9) for _ in xrange(_n)] for _ in xrange(_m)]
    
    def __repr__(self):
        return "Test()"
    def __str__(self):
        return "member of Test"


def expand_zeros(mat):
    pass


if __name__ == '__main__':
    _n = 10
    _m = 5
    mat = Matrix(_n, _m)
    print mat
    expand_zeros(mat)



