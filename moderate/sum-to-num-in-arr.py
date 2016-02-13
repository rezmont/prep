import random 

def arr_sum_to_num(arr, num):
    sorted_arr = sorted(arr)
    l = 0
    r = len(arr)-1
    while l<r:
        if sorted_arr[l] + sorted_arr[r] == num:
            print sorted_arr[l], sorted_arr[r]
            r -= 1
            l += 1
        elif sorted_arr[l] + sorted_arr[r] < num:
            l += 1
        else:  # arr[l] + arr[r] > num
            r -= 1


if __name__ == "__main__":
    arr = [random.randint(1,10) for _ in xrange(10)]
    num = 10
    print arr, num
    arr_sum_to_num(arr, num)