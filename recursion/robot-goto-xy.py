def ways_to_move_robot(dest, pos):
    if dest[0] == pos[0]:
        return 1
    elif dest[1] == pos[1]:
        return 1

    global book_keeping
    k = '{0}-{1}'.format(pos[0], pos[1])
    if k in book_keeping:
        return book_keeping[k]
    c = ways_to_move_robot(dest, (pos[0]+1, pos[1])) + ways_to_move_robot(dest, (pos[0], pos[1]+1))
    book_keeping[k] = c
    return c

if __name__ == '__main__':
    dest = (10, 10)
    book_keeping = {}
    print ways_to_move_robot(dest, (0, 0))