def fact_trailing_zero(n):
    no_fives = 0
    for i in xrange(1, n+1):
        j = i
        while j % 5 == 0:
            no_fives += 1
            j = j / 5
    return no_fives


if __name__ == '__main__':
    n = 10
    print fact_trailing_zero(n)