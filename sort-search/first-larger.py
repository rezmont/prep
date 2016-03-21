import random


def find_first_larger(arr, k):
    l = 0
    h = len(arr) - 1
    while l<=h:
        mid = l + (h-l)/2
        if arr[mid]==k:
            while mid < len(arr) and arr[mid] == k:
                mid += 1
            if mid == len(arr):
                return 'None'
            else:
                return arr[mid]
        if arr[mid] < k:
            l = mid + 1
        else:
            h = mid - 1

    while h < len(arr) and arr[h] < k:
        h += 1
    return arr[h]

if __name__ == '__main__':
    arr = sorted([random.randint(1,6) for _ in xrange(20)] + [random.randint(8,10) for _ in xrange(20)])
    x = find_first_larger(arr, 10)
    print arr
    print x