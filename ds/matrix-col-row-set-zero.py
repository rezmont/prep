import random


class Matrix(object):
    """docstring for Matrix"""
    def __init__(self, n, m, *args):
        self.mat = [[random.randint(0,9) for _ in xrange(_n)] for _ in xrange(_m)]
    
    def __repr__(self):
        return ' , \n'.join([str(row) for row in self.mat])
    # def __str__(self):
    #     return "member of Test"


    def expand_zeros(self):
        row_lst = []
        col_lst = []
        n = len(self.mat)
        m = len(self.mat[0])
        for i in xrange(n):
            for j in xrange(m):
                if self.mat[i][j] == 0:
                    row_lst.append(i)
                    col_lst.append(j)

        for i in row_lst:
            for j in xrange(m):
                self.mat[i][j] = 0

        for i in xrange(n):
            for j in col_lst:
                self.mat[i][j] = 0

if __name__ == '__main__':
    _n = 10
    _m = 5
    mat = Matrix(_n, _m)
    print mat
    mat.expand_zeros()
    print
    print mat



