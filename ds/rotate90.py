import random

class Matrix(object):
    """docstring for Matrix"""
    def __init__(self, n, *args):
        self.mat = [[random.randint(0,9) for _ in xrange(n)] for _ in xrange(n)]
    
    def __repr__(self):
        return ' , \n'.join([str(row) for row in self.mat])
    # def __str__(self):
    #     return "member of Test"


    def rotate90(self):
        n = len(self.mat)-1
        for i in xrange(n/2):
            for j in xrange(i, n-i):
                x0, y0 = i, j
                x1, y1 = trans(x0, y0, n)
                x2, y2 = trans(x1, y1, n)
                x3, y3 = trans(x2, y2, n)
                self.mat[x0][y0], self.mat[x1][y1], self.mat[x2][y2], self.mat[x3][y3] = self.mat[x3][y3], self.mat[x0][y0], self.mat[x1][y1], self.mat[x2][y2]

def trans(i, j, n):
    return j, n-i


if __name__ == '__main__':
    _n = 6
    mat = Matrix(_n)
    print mat
    mat.rotate90()
    print
    print mat



