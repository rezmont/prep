d = {
0: '',
1: 'one', 
2: 'two', 
3: 'three', 
4: 'four', 
5: 'five', 
6: 'six', 
7: 'seven', 
8: 'eight', 
9: 'nine', 
10: 'ten', 
11: 'evelven', 
12: 'twelve', 
13: 'thirteen', 
14: 'forteen', 
15: 'fifteen', 
16: 'sixteen', 
17: 'seventeen', 
18: 'eighteen', 
19: 'nineteen', 
20: 'twenty', 
30: 'thirty', 
40: 'fourty',
50: 'fifty',
60: 'sixty',
70: 'seventy',
80: 'eighty',
90: 'ninety',
}


def two_dig_to_word(a):
    # print a
    if a > 99:
        return False
    if a <= 20:
        return d[a]
    else:
        t = a / 10
        y = a - t * 10 
        t = t * 10
        return '{0} {1}'.format(d[t], d[y])

def three_dig_to_word(a):
    if a > 999:
        return False

    h = a / 100
    t = a - h * 100
    
    s0 = two_dig_to_word(t)
    s1 = ''
    if h>0:
        s1 = '{0} hundred'.format(d[h])
    
    if len(s1) > 0:
        return '{0} and {1}'.format(s1, s0)
    else:
        return '{0}'.format(s0)

def digit_to_word(num):
    orders = ['thousand ', 'million ', 'billion ']
    if num > 1000 * 1000 * 1000 * 1000:
        return False
    l = []

    for i, o in enumerate(orders):
        sub = num % 1000
        w = three_dig_to_word(sub)
        num = num / 1000        
        if num > 0:
            w = o + w
            l.append(w)
        else:
            l.append(w)
            break

    return ' '.join(l[::-1])



if __name__ == '__main__':
    num = 191
    print num
    print three_dig_to_word(num)

    num = 1942341
    print num
    print digit_to_word(num)