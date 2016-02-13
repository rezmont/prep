def largest_cont_sum(arr):
    l_sum = 0
    p_sum = 0
    for i in arr:
        print p_sum
        if p_sum + i > l_sum:
            l_sum = p_sum+i
        p_sum = p_sum+i
        if p_sum < 0:
            p_sum = 0

    return l_sum



if __name__ == '__main__':
    arr = [2, -8, 3, -2, 4, -10]
    print largest_cont_sum(arr)
