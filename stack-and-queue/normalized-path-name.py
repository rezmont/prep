
if __name__ == '__main__':
    path_name = '../home/motamedi/MEGA/../workspace//prep/../dasd/'
    tokens = path_name.split('/')
    s = []
    for el in tokens:
        # print el
        if el == '..':
            if len(s) == 0:
                raise Exception('Stack Empty Error')
            else:
                s.pop()
        elif el == '.' or el == '':  # ignore 
            pass
        else:
            s.append(el)

    print '/'.join(s)