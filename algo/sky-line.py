def merge_skyline(a, b):
    if len(a)==0:
        return b
    if len(b)==0:
        return a
    i = 0
    j = 0
    c = []
    ha_prev = 0
    hb_prev = 0 
    while i<len(a) and j<len(b):
        xa, ha = a[i] 
        xb, hb = b[j]
        if xa == xb:
            if ha >= hb:
                c.append((xa, ha))
            elif ha < hb:
                c.append((xb, hb))
            ha_prev = ha
            hb_prev = hb
            i += 1
            j += 1
        elif xa < xb:
            if ha >= hb_prev:
                c.append((xa, ha))
            else:
                if len(c)>0 and hb_prev > c[-1][1]:
                    c.append((xa, hb_prev))
            ha_prev = ha
            i += 1
        else:
            if ha_prev >= hb:
                if len(c)>0 and ha_prev > c[-1][1]:
                    c.append((xb, ha_prev))
                    # c.append((xb, ha_prev))
            else:
                c.append((xb, hb))
            hb_prev = hb
            j += 1
    while i < len(a):
        xa, ha = a[i] 
        c.append((xa, ha))        
        i += 1
    while j < len(b):
        xb, hb = b[j] 
        c.append((xb, hb))        
        j += 1

    return c

if __name__ == '__main__':
    a = [(1, 10), (2, 0)]
    b = [(3, 20), (4, 0)]
    c = merge_skyline(a, b)
    print c