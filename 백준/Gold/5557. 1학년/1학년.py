import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

'''
왼쪽부터 계산할 때, 중간에 나오는 수가 모두 0 이상 20 이하이어야 한다.
'''
# dp = [[] for _ in range(n-1)]
# dp[0].append(data[0])

check = [0 for i in range(21)]

check[data[0]] += 1

idx = 1
cnt = 0

while idx < n-1:
    my_check = [0 for i in range(21)]

    for i in range(21):
        if check[i]:
            if i + data[idx] <= 20:
                my_check[i + data[idx]] += check[i]
            if i - data[idx] >= 0:
                my_check[i - data[idx]] += check[i]

    # print(idx, data[idx], my_check)
    check = my_check
    idx += 1

print(check[data[-1]])
