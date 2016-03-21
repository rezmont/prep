import random

def selection_sort(arr):
    l = len(arr)
    left = l-1
    while left > 0:
        max_index = left
        for i in xrange(left, -1, -1):
            if arr[max_index][0] < arr[i][0]:
                max_index = i
        if max_index != left:
            tmp = arr[max_index]
            arr[max_index:left] = arr[max_index+1:left+1] 
            # for i in xrange(max_index, left):
            #     arr[i] = arr[i+1]
            arr[left] = tmp
            print arr[left], '>>', arr
        left -= 1
    return



if __name__ == '__main__':
    arr = [(random.randint(0, 5), i) for i in xrange(10)]
    print arr
    selection_sort(arr[:])
    print arr