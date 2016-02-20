def combination(string):
    if len(string) == 1:
        return [[], [string]]

    l = []
    el = string[0]
    inner_l = combination(string[1:])
    for item in inner_l:
        # print item
        l.append(item)
        l.append(item+[el])
        print item, el
    # print 'l', l
    return l
        


if __name__ == "__main__":
    a = '12'
    print combination(a)
