import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
ans = max(dp)
print(ans)

result = []
idx = ans
for i in range(n-1, -1, -1):
    if dp[i] == idx:
        result.append(A[i])
        idx -= 1
print(*result[::-1])
