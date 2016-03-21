import hashlib


if __name__ == '__main__':
    s = 'ali'
    h = 1
    for c in s:
        x = hashlib.md5(c).hexdigest()
        print x, type(x), int(x, 16)