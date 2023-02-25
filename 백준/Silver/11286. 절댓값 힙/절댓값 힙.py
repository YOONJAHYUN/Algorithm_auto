import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (abs(x), int(x/abs(x))))

    else:
        if heap:
            a, b = heapq.heappop(heap)
            print(a*b)

        else:
            print(0)
