import random


def reassign_saleries(arr, k):
    new_saleries = list()
    i = 0
    rem = k
    while i < len(arr) and rem > 0:
        if rem / (len(arr) - i) > arr[i]:
            new_saleries.append(arr[i])
            rem -= arr[i]
            i += 1
        else:
            break
    eq_share = 1.0 * rem / (len(arr) - i)
    while i<len(arr):
        new_saleries.append(eq_share)
        i += 1
    return new_saleries


if __name__ == '__main__':
    arr = sorted(set([random.randint(10, 100) for _ in xrange(20)]))
    s = sum(arr)
    print s, arr
    new_arr = reassign_saleries(arr, s-30)
    print sum(new_arr), new_arr