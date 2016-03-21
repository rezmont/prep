import random
    
def calc_interval_union(bar):
    arr = [(j, k) for el in bar for k, j in enumerate(el)]
    sorted_arr = sorted(arr)
    cnt = 0
    events = []
    for t, e in sorted_arr:
        past_cnt = cnt
        if e == 0:
            cnt += 1
        else:
            cnt -= 1
        if past_cnt == 0 and cnt != 0:
            events.append('[{0}..'.format(t))
        elif past_cnt != 0 and cnt == 0:
            events.append('..{0}]'.format(t))
    print events

if __name__ == '__main__':
    foo = [(random.randint(0,100), random.randint(1,5)) for _ in xrange(100)]
    bar = [(a, a+b) for a, b in foo]
    calc_interval_union(bar)
