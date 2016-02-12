def insert_parans2(exp, lvl):
    # print exp
    global books
    if len(exp) == 1:
        return [exp]
    if len(exp) == 2:
        print exp
        return 'ERR'

    if exp in books:
        return books[exp]
    l = []
    for i, el in enumerate(exp):
        if el in {'|', '^', '&'}:
            l1 = insert_parans2(exp[:i], lvl+1)
            l2 = insert_parans2(exp[i+1:], lvl+1)
            for el1 in l1:
                for el2 in l2:
                    l.append('({0}{1}{2})'.format(el1, el, el2))


    books[exp] = l
    global result
    ret_result = []
    if lvl == 0:
        for el in l:
            if eval(el) == result:
                ret_result.append(el)
        return ret_result 
    else:
        return l



    # if len(exp) == 0: 
    #     while len(s)>=3:
    #         param2 = s.pop()
    #         operand = s.pop()
    #         param1 = s.pop()
    #         s.append('({0}{1}{2})'.format(param1, operand, param2))
    #     if len(s) == 1:
    #         res_exp = s.pop()
    #         if eval(res_exp) == result:
    #             print '>', res_exp
    
    # if len(exp) >= 3 and exp[0] in {'0', '1'}:
    #     s_aux = s[:] 
    #     s_aux.append('({0})'.format(exp[0:3]))
    #     insert_parans(s_aux, exp[3:])

    # if len(exp) >= 2:
    #     s_aux = s[:] 
    #     s_aux.append(exp[0])
    #     s_aux.append(exp[1])
    #     insert_parans(s_aux, exp[2:])


def insert_parans(s, exp):
    global result
    if len(exp) == 0: 
        while len(s)>=3:
            param2 = s.pop()
            operand = s.pop()
            param1 = s.pop()
            s.append('({0}{1}{2})'.format(param1, operand, param2))
        if len(s) == 1:
            res_exp = s.pop()
            if eval(res_exp) == result:
                print '>', res_exp
    
    if len(exp) >= 3 and exp[0] in {'0', '1'}:
        s_aux = s[:] 
        s_aux.append('({0})'.format(exp[0:3]))
        insert_parans(s_aux, exp[3:])

    if len(exp) >= 2:
        s_aux = s[:] 
        s_aux.append(exp[0])
        s_aux.append(exp[1])
        insert_parans(s_aux, exp[2:])


def insert_parans_WRONG(exp, pos, open_parans, remaining_parans):
    global result
    print exp, remaining_parans
    raw_input('...')
    if pos == len(exp) and open_parans == 0:
        val = eval(exp)
        if val == result:
            print '>>', exp

    if remaining_parans<0:
        return False

    for i in xrange(pos, len(exp)):
        exp_aux = '{0}({1}'.format(exp[:pos], exp[pos:])
        insert_parans(exp_aux, pos+1, open_parans+1, remaining_parans-1)
        
        if pos>0 and exp[pos-1] != '(' and exp[pos-1] != ')' and open_parans>0:
            exp_aux = '{0}){1}'.format(exp[:pos], exp[pos:])
            insert_parans(exp_aux, pos+1, open_parans-1, remaining_parans)

        insert_parans(exp, pos+1, open_parans, remaining_parans)



if __name__ == '__main__':
    no_operators = 0
    exp = '1^0|0|1'
    result = False

    # s = []
    # insert_parans(s, exp)

    print exp
    books = {}
    lst = insert_parans2(exp, 0)
    print lst
