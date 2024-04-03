import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
n = str(n)
m = len(n)

if m == 1:
    print(-1)
    exit(0)

q = deque()
q.append((n, 0))
answer = -1
visited = dict()

flag = 0
while q:

    number, cnt = q.popleft()

    if cnt == k:
        answer = max(answer, int(number))
        continue

    if flag != cnt:
        flag = cnt
        visited = dict()

    lst = []
    lst.extend(number)
    for i in range(m):
        for j in range(i+1, m):
            lst[i], lst[j] = lst[j], lst[i]
            new_number = (''.join(map(str, lst)))
            if not visited.get(new_number) and new_number[0] != '0':
                q.append((new_number, cnt+1))
                visited[new_number] = 1
            lst[i], lst[j] = lst[j], lst[i]

print(answer)
