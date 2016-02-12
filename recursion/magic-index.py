def find_magic_index_no_duplicates(arr, offset):
    if len(arr) == 0:
        return False
    elif len(arr) == 1:
        if arr[0] == offset:
            return arr[0]
        else:
            False
    print arr, offset
    mid = len(arr)/2
    if mid+offset == arr[mid]:
        return arr[mid]
    elif mid+offset < arr[mid]:
        x = find_magic_index_no_duplicates(arr[:mid], offset)
        if x != False:
            return x
    else:
        x = find_magic_index_no_duplicates(arr[mid+1:], offset+mid+1)
        if x != False:
            return x
    return False

def find_magic_index_with_duplicates(arr, offset):
    if len(arr) == 0:
        return False
    elif len(arr) == 1:
        if arr[0] == offset:
            return arr[0]
        else:
            False

    print arr, offset
    raw_input('...')

    mid = len(arr)/2
    if mid+offset == arr[mid]:
        return arr[mid]
    
    x = find_magic_index_with_duplicates(arr[:min(mid, arr[mid])], offset)
    if x != False:
        return x

    x = find_magic_index_with_duplicates(arr[max(mid+1, arr[mid]):], offset+max(mid+1, arr[mid]))
    if x != False:
        return x
    return False


if __name__ == '__main__':
    arr = [-1, 0, 3, 3, 7]
    print find_magic_index_with_duplicates(arr, 0)