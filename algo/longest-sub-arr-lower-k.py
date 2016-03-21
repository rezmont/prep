

def longest_sub_arr_sum_lower_k(arr, k):
    if len(arr) == 1:
        if arr[0]:
            return arr[0], 1, 1
        else:
            return 0, 0, 0
    s, len_inc, len_exc = longest_sub_arr_sum_lower_k(arr[1:], k)
    if (s+arr[0]) < 0