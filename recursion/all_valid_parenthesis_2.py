def all_proper_parans(n, num_open, s):
    # print n, num_open, s
    if n < 0:
        return
    if n == 0 and num_open==0:
        print s
        return
    if num_open > 0:
        all_proper_parans(n, num_open-1, s+')')
    all_proper_parans(n-1, num_open+1, s+'(')

      
all_proper_parans(3, 0, '')