def grid_print(grid):
    print '\n'.join([str(el) for el in grid])


def is_a_valid_grid(grid):
    q = []
    n = len(grid)
    """ Rows and Columns """
    s_row = [0 for _ in xrange(n)]
    s_col = [0 for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            s_row[i] += grid[i][j]
            s_col[j] += grid[i][j]
            if grid[i][j]:
                q.append((i,j))
    for i in xrange(n):
        if s_row[i] > 1 or s_col[i] > 1:
            # print s_row, s_col
            return False
    
    """ Diagnoal """
    for i, q1 in enumerate(q):
        for j, q2 in enumerate(q):
            if i != j and abs(q1[0]-q2[0]) == abs(q1[1]-q2[1]):
                return False
    return True 

def eight_queens(grid, i):
    # print 'i:', i
    # grid_print(grid)
    # raw_input('...')

    n = len(grid)
    good = is_a_valid_grid(grid);
    if not good:
        # print 'bad'
        return False
    
    if i == 8:
        grid_print(grid)
        raw_input('...')
        return True

    for j in xrange(n):
        grid[i][j] = 1
        eight_queens(grid[:][:], i+1) 
        grid[i][j] = 0


if __name__ == '__main__':
    grid = [[0 for _ in xrange(8)] for _ in xrange(8)]
    grid_print(grid)
    print
    eight_queens(grid, 0)