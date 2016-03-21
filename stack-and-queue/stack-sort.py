import random


def stack_sort(arr):
    print arr
    raw_input('...')
    if len(arr) == 1:
        return

    t = arr.pop()
    stack_sort(arr)
    insert_t_on_s(arr, t)

def insert_t_on_s(arr, t):
    print arr, t
    raw_input('---')
    if len(arr)==0:
        arr.append(t)
    elif t <= arr[-1]:
        arr.append(t)
    else:
        tmp = arr.pop()
        insert_t_on_s(arr, t)
        insert_t_on_s(arr, tmp)
    
if __name__ == '__main__':
    arr = [random.randint(1,100) for _ in xrange(4)]
    stack_sort(arr)
    print arr