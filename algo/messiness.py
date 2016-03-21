import random

def messiness(txt, index):
    global mem
    if index == 0:
        return 0

    if index in mem:
        return mem[index]
    # if index == 1:
    #     b = 80 - len(txt[index])
    #     mem[index] = 2 ** b
    #     return 2 ** b

    i = 1
    s = txt[index-i]
    print index, s
    raw_input('...')
    min_mess = messiness(txt, index-i) + 2 ** (80 - len(s))
    i += 1
    while len(s) <= 80 and index-i>=0:
        s = txt[index-i] + ' '+ s 
        print index, s
        raw_input('...')
        m = messiness(txt, index-i) + 2 ** (80 - len(s))
        if min_mess > m:
            min_mess = m
        i += 1

    mem[index] = min_mess
    return min_mess



if __name__ == '__main__':
    mem = {}
    txt = [str(i)*random.randint(1, 10) for i in xrange(10)]
    # txt = ['0000000', '1111111', '2']
    print txt
    mess = messiness(txt, len(txt))
    print mess
    print mem
    l = len(' '.join(txt))
    print txt, l, 2 ** (80 - l)