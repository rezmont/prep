def swap_odd_even_bits(a):
    print bin(a)
    mask1=1
    mask2=2
    x = 0
    while a>mask1:
        x = x ^ ((a & mask1) << 1)
        x = x ^ ((a & mask2) >> 1)
        mask1 = mask1 << 2
        mask2 = mask2 << 2
    print bin(x)

if __name__ == '__main__':
    val = 111
    swap_odd_even_bits(val)    