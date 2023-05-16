import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

start = 0
end = n-1

ans = 2000000000
result = []

while start < end:

    a = data[start]
    b = data[end]

    my_sum = a+b
    if abs(my_sum) < ans:
        ans = abs(a+b)
        result = [a, b]

        if ans == 0:
            break

    if my_sum < 0:
        start += 1
    else:
        end -= 1

print(*result)