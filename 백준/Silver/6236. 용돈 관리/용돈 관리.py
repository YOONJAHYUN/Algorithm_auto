import sys
input = sys.stdin.readline


n, m = map(int, input().split())

data = [int(input()) for _ in range(n)]
# print(data)

start = max(data)
end = sum(data)

ans = end
vm = start

while start <= end:

    # 인출금액 k = mid인지
    mid = (start+end) // 2

    current = data[0]
    count = 1
    for i in range(1, n):
        if current + data[i] > mid:
            count += 1
            current = data[i]
        else:
            current += data[i]

    if count > m:
        start = mid + 1
        # if count == m:
        #     ans = max(mid, ans)
    else:
        end = mid - 1
        if mid >= vm:
            ans = min(mid, ans)

print(ans)