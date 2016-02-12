import random


def make_tower(a):
    if len(a) == 1:
        return a[0][0], a

    max_h = 0
    max_h_vec = []
    for i, el in enumerate(a):
        # print el
        arr_aux = [el_aux for el_aux in a if el_aux[0]<el[0] and el_aux[1]<el[1]]
        if len(arr_aux)>0:
            # print '>', arr_aux
            h, vec = make_tower(arr_aux)
            # print '>>', vec
            if h + el[0] > max_h:
                max_h = h + el[0]
                max_h_vec = [el] + vec 
                # print [el] + vec 
        else:
            if el[0] > max_h:
                max_h = el[0]
                max_h_vec = [el]

    # print '#', max_h, max_h_vec
    return max_h, max_h_vec


def comp(a, b):
    return a[0]<b[0] and a[1]<b[1]

def conunt_longest_nondecrease(a):
    

if __name__ == '__main__':
    a = [(62, 170), (74, 93), (78, 173), (74, 158), (68, 176), (62, 147), (79, 153), (65, 162), (61, 161), (77, 121)]
    # print a
    # print make_tower(a)


    # a = [(random.randint(60,80), random.randint(90, 190)) for _ in xrange(10)]
    b = sorted(a, cmp=comp)
    print a
    print b
