from collections import Counter

def first_non_repeated(string):
    cnts = Counter(string)
    for c in string:
        if cnts[c] == 1:
            print c 
            return
    print 'False'

if __name__ == '__main__':
    string  = 'total'
    first_non_repeated(string)