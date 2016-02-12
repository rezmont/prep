def frac_to_bin(num):
    ret = []
    base = 0.5
    while num > 0:
        # print num
        # raw_input('...')
        if num >= base:
            ret.append('1')
            num -= base
        else:
            ret.append('0')
        base /= 2
    
    if len(ret)<=32:
        return ''.join(ret)
    else:
        print '>>', ''.join(ret)
        return 'ERROR'


if __name__ == '__main__':
    x = 0.5
    print frac_to_bin(x)
    x = 0.7
    print frac_to_bin(x)