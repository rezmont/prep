


def rotate_array(arr, k):
    if k > len(arr):
        k = k % len(arr)
    already_done = set()
    i = 0
    cnt = 0
    while len(already_done) < k:
        print i
        already_done.add(i)
        starting_point = i 
        tmp = arr[i]
        i = i+k
        while i!= starting_point:
            cnt += 1
            tmp, arr[i] = arr[i], tmp
            i = (i+k) % len(arr)
            if i<k:
                already_done.add(i)
        tmp, arr[i] = arr[i], tmp
        cnt += 1
        while i in already_done:
            i = (i+1) % len(arr)
    print already_done
    print cnt


if __name__ == '__main__':
    arr = [i for i in xrange(10)]
    print arr
    rotate_array(arr, 100)
    print arr