import sys
from heapq import heappop, heappush

input = sys.stdin.readline

# n 보석의 개수, k 가방
n, k = map(int, input().split())
# m 무게 v 가격
data = [tuple(map(int, input().split())) for _ in range(n)]
data.sort()

bags = [int(input()) for _ in range(k)]
bags.sort()

ans = 0
temp = []
# 가방무게만큼
for c in bags:
    # 가장 가벼운거랑 비교
    while data and c >= data[0][0]:
        # 제일 가벼운걸 꺼냄
        weight, value = heappop(data)
        # 그리고 정렬함, 높은가격순으로
        heappush(temp, (-value))
    if temp:
        # 가장 높은 가격을 더해줌
        ans -= heappop(temp)

print(ans)
