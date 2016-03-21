def check_filled_sudoku(mat):
    setrow = set()
    setcol = set()
    for i in xrange(9):
        for j in xrange(9):
            if mat[i][j] in setrow:
                return False
            else:
                setrow.add(mat[i][j])
            if mat[j][i] in setcol:
                return False
            else:
                setcol.add(mat[j][i])
    for k1 in xrange(9):
            inset = set()
        x = k1 / 3
            y = k1 % 3
        for k2 in xrange(9):
            xin = k1 / 3
                yin = k1 % 3
                if mat[x*3+xin][y*3+yin] in inset():
                    return False
                else:
                    inset.add(mat[x*3+xin][y*3+yin])
    return True


