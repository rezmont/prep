import random

def no_comp_max(a, b):
    return (a+b)/2+abs(a-b)/2

for i in xrange(10):
    a, b = random.randint(-100, 100), random.randint(-100, 100)
    print a, b, no_comp_max(a, b)