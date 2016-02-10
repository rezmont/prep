def string_zip(s):
    zipped = [] 
    last = ''
    cnt = 0
    for el in s:
        if len(last) == 0:
            last= el
            cnt = 1
        elif last == el:
            cnt += 1
        else:
            zipped.append('{0}{1}'.format(last, cnt))
            last = el
            cnt = 1
    else:
        zipped.append('{0}{1}'.format(last, cnt))
        last = el
        cnt = 1

    zipped_string = ''.join(zipped)
    if len(zipped_string) > len(s):
        print 'rejecting', zipped_string 
        return s
    else:
        return zipped_string


if __name__ == '__main__':
    s = 'ewrwerwdsaddsdsaaa'
    print string_zip(s)

    s = 'aabcccccaaa'
    print string_zip(s)