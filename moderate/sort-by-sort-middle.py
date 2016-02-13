def is_in_sorted_pos(arr, num, pos):
    sm = 0
    eq = 0
    i = 0 
    for i, v in enumerate(arr):
        if v < num:
            sm += 1
        elif v == num:
            eq += 1

    if sm <= pos and pos <= sm+eq:
        return True
    else:
        return False


def find_pivots(arr):
    arr_len = len(arr)

    l = 1
    while l+1 < arr_len and arr[l] < arr[l+1]:
        l += 1

    r = arr_len - 1
    while r-1 > 0 and arr[r] > arr[r-1]:
        r -= 1

    l -= 1
    while not is_in_sorted_pos(arr, arr[l], l):
        l -= 1
    l += 1

    r += 1
    while not is_in_sorted_pos(arr, arr[r], r):
        r += 1
    r -= 1

    print l, r


def is_in_sorted_pos_adjacent(arr, pos):
    no_correct_pos = 0
    num = arr[pos]
    sm = 0
    eq = 0
    i = 0 
    for i, v in enumerate(arr):
        if v < num:
            sm += 1
        elif v == num:
            eq += 1

    if sm <= pos and pos <= sm+eq:
        no_correct_pos += 1
    
    pos = pos+1
    num = arr[pos]
    sm = 0
    eq = 0
    i = 0 
    for i, v in enumerate(arr):
        if v < num:
            sm += 1
        elif v == num:
            eq += 1

    if sm <= pos and pos <= sm+eq:
        no_correct_pos += 1

    return no_correct_pos

if __name__ == '__main__':
    arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    find_pivots(arr)