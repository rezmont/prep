

def bin_2d_search(mat, v,  lx, hx, ly, hy):
    midx = (lx + hx) / 2 
    midy = (ly + hy) / 2
    pass

if __name__ == '__main__':
    mat = []
    for i in xrange(20):
        mat.append([j for j in xrange(i,i+10)])
    print '\n'.join([str(el) for el in mat])

    bin_2d_search(mat, 2, 0, len(mat[0]), 0, len(mat))