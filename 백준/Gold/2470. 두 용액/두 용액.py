import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

data.sort()
ans = 10000000000000
result = []

left, right = 0, N-1

while left < right:

    my_left = data[left]
    my_right = data[right]

    total = my_left + my_right

    # 일단 지금까지 구한것 보다 작다면 담기
    if abs(total) < ans:
        ans = abs(total)
        result = [my_left, my_right]

    if total < 0:
        left += 1
    else:
        right -= 1

print(*result)
