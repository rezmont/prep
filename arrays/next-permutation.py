def calc_next_perm(arr):
    l = len(arr)
    next_arr = [-1 for _ in xrange(l)]
    tracker = [i for i in xrange(l)]
    pos = l-1
    while pos>=0:
        if pos == l-1:
            next_perm_el = (arr[pos]+1) % l
        else: 
            next_perm_el = arr[pos]
        # print next_perm_el
        while tracker[next_perm_el] != next_perm_el:
            next_perm_el = (next_perm_el+1) % l

        next_arr[pos] = next_perm_el
        tracker[next_perm_el] = -1
        pos -= 1
    if next_arr > arr:
        return next_arr
                

                    
if __name__ == '__main__':
    # arr = [9-i for i in xrange(10)]
    arr = [1, 0, 3, 2]
    print arr
    ret = calc_next_perm(arr)
    print ret