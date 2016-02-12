if __name__ == '__main__':
    n = 0b1000000000000000
    m = 0b10011
    i = 2
    j = 6

    mask = m << i
    result = n | mask
    print bin(result)