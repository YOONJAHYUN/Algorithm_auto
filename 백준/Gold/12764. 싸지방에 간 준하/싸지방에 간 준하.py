import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    p, q = map(int, input().split())
    heappush(data, (p, q))

computers = [0] * (n)
count = [0] * (n)

turn = 1

# 순서, 끝나는 시간, 이용자 수
cnt = 0
while data:
    next = heappop(data)

    for i in range(n):
        # 넣을 수 있으면
        if computers[i] <= next[0]:
            # 아직 아무도 안옴
            if computers[i] == 0:
                cnt += 1
            computers[i] = next[1]
            count[i] += 1
            break

print(cnt)

for i in count:
    if i != 0:
        print(i, end=" ")

        