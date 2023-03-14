import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())

data = list(map(int, input().split()))
data.sort()
lst = list(permutations(data, M))

for i in lst:
    print(*i)

