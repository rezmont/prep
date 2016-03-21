
def search_helper(mat, arr, i, j):
    global mem
    if len(arr) == 0:
        return True
    key = '{0}{1}{2}'.format(i, j, arr)
    if key in mem:
        return mem[key]
    for d in [-1, 1]:
        if i+d > 0 and i+d < len(mat) and mat[i+d][j] == arr[0]:
            h = search_helper(mat, arr[1:], i+d, j)
            if h == True:
                return True
        if j+d > 0 and j+d < len(mat) and mat[i][j+d] == arr[0]:
            v = search_helper(mat, arr[1:], i, j+d)
            if v == True:
                return True
    mem[key] = False


def search(mat, arr):
    for i in xrange(len(mat)):
        for j in xrange(len(mat[0])):
            if mat[i][j] == arr[0]:
                ret = search_helper(mat, arr[1:], i, j)
                if ret == True:
                    return True
    return False



if __name__ == '__main__':
    mat = [[1, 2, 3], [3, 4, 5], [5,  6, 7]]
    arr = [1, 2, 3, 4]
    mem = {}
    r = search(mat, arr)
    print r