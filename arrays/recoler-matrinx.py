def recoler_mat(mat, i, j, c):
    if mat[i][j] == c:
        return
    mat[i][j] = c
    size = len(mat)
    d = [-1, 1]
    for v in d:
        if i+v > 0 and i+v < size:
            recolor_mat(mat, i, j+h, c)

    for h in d:
        if j+h > 0 and j+h < size:
            recolor_mat(mat, i+v, j, c)

