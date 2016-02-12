def all_valid_paranthesis(n):
    if n==1:
        return ['()']

    global book_keeping

    if n-1 in book_keeping:
        return book_keeping[n]
    l = all_valid_paranthesis(n-1)
    ret_list = []
    for el in l:
        ret_list.append('(){0}'.format(el))
        ret_list.append('({0})'.format(el))
        if el[:2]!='()':
            ret_list.append('{0}()'.format(el))

    book_keeping[n] = ret_list
    return ret_list



if __name__ == '__main__':
    book_keeping = {}
    n = 4
    l = all_valid_paranthesis(n)
    print '\n'.join(l)
    print len(l)


n=4
def pc(p,i):
    if i<n:
            pc(p+'{}',i+1)
            pc('{'+p+'}',i+1)
            if(p[:2]!='{}'):
                    pc('{}'+p,i+1)
    else:
            print p
pc('{}',1)