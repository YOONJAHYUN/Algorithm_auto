import sys
input = sys.stdin.readline

n = int(input())
m = int(n**0.5)

dp = [i for i in range(n+1)]

for i in range(2, m+1):
    for j in range(1, n+1):
        if j >= i*i:
            dp[j] = min(dp[j], dp[j-i*i]+1)
print(dp[n])