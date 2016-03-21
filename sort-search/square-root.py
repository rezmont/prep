import math

def squre_root(arg):
    i = 1
    step = 1
    while step > 0.000000001:
        while (i+step)*(i+step) > arg:
            if (i+step)*(i+step) ==  arg:
                return i+step
            step = step / 2.0
        i += step
    return i

if __name__ == '__main__':
    num = 2
    s = squre_root(num)
    print s
    print math.sqrt(num)