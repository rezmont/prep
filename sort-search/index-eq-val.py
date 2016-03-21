# i 10
# v 100


# i 100
# v 10


import random

def find_index_eq_val(arr):
    l = 0
    h = len(arr) -1
    while l <= h:
        mid = l + (h-l)/2
        if arr[mid] == mid:
            return mid
        if arr[mid] < mid:
            h = mid - 1
        else:
            l = mid + 1
    return 'None'

if __name__ == '__main__':
    arr = sorted(set([random.randint(-100, 100) for _ in xrange(20)]))
    x = find_index_eq_val(arr)
    print arr
    print x