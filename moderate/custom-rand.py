import random 
import matplotlib.pyplot as plt 
import numpy as np

def random7():
    vec = []
    for _ in xrange(1000000):
        x = 5 * random.randint(0, 4) + random.randint(0, 4)
        vec.append(x)

    binwidth = 1
    plt.hist(vec, bins=np.arange(0, 25 + binwidth, binwidth)-0.5)
    plt.show()


if __name__ == '__main__':
    # print np.arange(0, 12) + 0.5
    print random7()