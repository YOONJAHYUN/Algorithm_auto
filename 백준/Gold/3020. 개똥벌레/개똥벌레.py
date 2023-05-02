import sys
input = sys.stdin.readline

n, h = map(int, input().split())

result = [0] * h

for i in range(n):
    high = int(input())
    if i%2:
        result[high] -= 1
        result[0] += 1
    else:
        result[h-high] += 1

# 누적합을 따로
for i in range(1, h):
    result[i] += result[i-1]

my_min = (n+1)
cnt = 0
for i in range(h):
    if my_min > result[i]:
        my_min = result[i]
        cnt = 1
    elif my_min == result[i]:
        cnt += 1
print(my_min, cnt)
