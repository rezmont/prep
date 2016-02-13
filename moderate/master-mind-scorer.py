def calc_score(a, b):
    
    hint = 0
    psuedo_hint = 0
    rem_a = {}
    rem_b = {}
    for i, j in zip(a, b):
        if i==j:
            hint += 1
        else:
            if i in rem_a:
                cnt = rem_a[i]
                rem_a[i] = cnt+1 
            else:
                rem_a[i] = 1
            
            if j in rem_b:
                cnt = rem_b[j]
                rem_b[i] = cnt+1 
            else:
                rem_b[j] = 1
            
    for k, v in rem_a.iteritems():
        if k in rem_b:
            psuedo_hint += min(rem_a[k], rem_b[k])
    print a, b, rem_a, rem_b
    print '>>', hint, psuedo_hint


if __name__ == '__main__':
    a = 'GGRR'
    b = 'RGBY'
    calc_score(a, b)