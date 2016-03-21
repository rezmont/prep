def show_k_cents(k, i, res):
    global mem
    if k == 0:
        print res
        return 1
    if k < 0 or i>3:
        return 0

    key = '{0},{1}'.format(k, i)
    # if key in mem:
    #     return mem[key]

    c = 0
    vec = [1, 5, 10, 25]
    num = 0
    while vec[i]*num <= k:
        c += show_k_cents(k-(vec[i]*num), i+1, res+', {0}*{1}'.format(num, vec[i]))
        num += 1
    mem[key] = c
    return c


mem = {}
show_k_cents(25, 0, '')
