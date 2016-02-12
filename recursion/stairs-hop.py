def count_possible_jumps(n):
    if n == 1:
        return 1
    if n == 2:
        return 2  # 1+1, 2
    if n == 3:
        return 4  # 1+1+1, 2+1, 1+2, 3

    global book_keeper
    if n in book_keeper:
        return book_keeper[n]

    c = count_possible_jumps(n-1)+count_possible_jumps(n-2)+count_possible_jumps(n-3)
    book_keeper[n] = c
    return c
    
def count_possible_jumps_iterative(n):
    pass    

if __name__ == '__main__':
    n = 10
    book_keeper = {}
    print count_possible_jumps(n)
    print book_keeper