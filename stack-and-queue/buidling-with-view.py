import random

def east_to_west(arr):
    s = []
    for i in arr:    
        while len(s)>0 and i>=s[-1]:
            s.pop()
        s.append(i)
    return s


def west_to_east(arr):
    if len(arr)==0:
        return False
    s = [arr[0]] 
    for i in arr[1:]:
        if i>s[-1]:
            s.append(i)
    return s[::-1]


if __name__ == '__main__':
    arr = [random.randint(1,100) for _ in xrange(50)]
    print east_to_west(arr)
    print west_to_east(arr[::-1])
