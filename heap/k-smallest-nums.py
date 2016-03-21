import heapq
import math

if __name__ == '__main__':
    h = []
    k = 10
    for i in xrange(k):
        for j in xrange(k-i):
            v = i+math.sqrt(2)*j
            if len(h) < k:
                heapq.heappush(h, v)
            else:
                if v < h[0]:
                    heapq.replcae(h, v)
                else:
                    break

    print h