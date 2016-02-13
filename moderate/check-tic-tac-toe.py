import random

def print_grid(grid):
    print '\n'.join([str(l) for l in grid])

def check_if_won(grid):
    """row"""

    for i in xrange(3):
        set_row = set()
        set_col = set()
        for j in xrange(3):
            set_row.add(grid[i][j])
            set_col.add(grid[j][i])

        if len(set_row)==1:
            return list(set_row)[0]
        if len(set_col)==1:
            return list(set_col)[0]

    set_diag1 = set()
    set_diag2 = set()
    for i in xrange(3):
        set_diag1.add(grid[i][i])
        set_diag2.add(grid[2-i][i])

    if len(set_diag1)==1:
        return list(set_diag1)[0]
    if len(set_diag2)==1:
        return list(set_diag2)[0]



if __name__ == '__main__':
    grid = [[ random.randint(0,2) for _ in xrange(3)] for _ in xrange(3)]
    print grid
    print_grid(grid)

    print check_if_won(grid)