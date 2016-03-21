import random

def inplace_qsort(arr, l, r):
    print arr, l, r
    raw_input('...')
    if l + 1 >= r:
        return

    l_pos = l
    r_pos = r
    pivot = arr[l]
    eq_cnt = 0
    i = r
    while l_pos + eq_cnt < i:
        if pivot == arr[i]:
            eq_cnt += 1
            i -= 1
        elif pivot < arr[i]:
            arr[r_pos] = arr[i]
            i -= 1
            r_pos -= 1
        else:
            arr[l_pos], arr[i] = arr[i], arr[l_pos]
            l_pos += 1
    for i in xrange(l_pos, r_pos):
        arr[i] = pivot
    print pivot, arr, l, l_pos, r_pos, r 

    inplace_qsort(arr, l, l_pos)
    inplace_qsort(arr, r_pos, r) 


if __name__ == '__main__':
    # arr = [random.randint(1, 7) for _ in xrange(10)]
    arr = [2, 1, 3, 4, 1, 6, 2, 3, 6, 4]
    print arr
    inplace_qsort(arr, 0, len(arr)-1)
    print arr
    print sorted(arr)