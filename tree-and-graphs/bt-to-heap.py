import random


def heapify(a, l):
    if (l*2)+1 >= len(a): 
        return -1
    elif (l*2)+1 == len(a) - 1:
        x, y = a[l], a[2*l + 1]
        if x > y:
            a[l], a[2*l + 1] = y, x
            return l
        else:
            return -1

    left = 2*l + 1
    x, y, z = a[l], a[left], a[left+1] 
    if y < x and y < z:
        a[l], a[left] = y, x
        return l
    if z < x and z < y:
        a[l], a[left+1] = z, x
        return l
    else:
        return -1
            


if __name__ == '__main__':
    arr = [random.randint(1, 10) for _ in xrange(10)]
    arr[0] = 100
    arr[9] = 0
    print arr
    
    for i in xrange(10):
        l = i
        while l >= 0:
            # print i, l
            l = heapify(arr, l)
            # print l, arr
            l = (l-1)/2

    print arr