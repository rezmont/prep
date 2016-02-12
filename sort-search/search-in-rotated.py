def rotate(a, n):
    for j in xrange(n):
        tmp = a[-1]
        for i in xrange(len(a)-1, -1, -1):
            a[i] = a[i-1]
        a[0] = tmp
    return a

def rotate2(a, n):
    rotated = set() 
    j = 0
    while len(rotated) < n:
        # print a, rotated
        if j in rotated:
            j = (j + 1) % n
            continue
        rotated.add(j)
        
        tmp = a[j] 
        j = j+n
        
        other_cycles = []
        while j not in rotated:
            # print tmp, j, '>', a
            tmp, a[j] = a[j], tmp
            j = j+n 
    
            if j >= len(a):   
                j = j - len(a)
                # tmp, a[j] = a[j], tmp
                other_cycles.append(j)

        a[j] = tmp
        # print '>>>', rotated
        rotated = rotated.union(set(other_cycles))
        # print '>>>', rotated
    return a

def search(a, x):
    left = 0
    right = len(a)
    
    while left<right:
        print left, right, a[left:right]
        mid = (left+right)/2
        if a[mid]==x:
            return mid

        if a[left] < a[mid]:
            if a[left] < x and x < a[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if a[left] < x or a[mid] > x:
                right = mid-1
            else:
                left = mid+1

    return False

if __name__ == '__main__':
    a = range(8)
    n = 4
    print a
    a = rotate2(a, n)
    print a

    print search(a, 3)