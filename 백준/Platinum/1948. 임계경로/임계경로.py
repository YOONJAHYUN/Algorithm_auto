import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    q = deque()
    times = [0] * (n+1)

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # result = []

    while q:

        now = q.popleft()
        # result.append(now)

        for time, next in graph1[now]:
            indegree[next] -= 1
            times[next] = max(times[next], times[now]+time)
            if indegree[next] == 0:
                q.append(next)

    print(times[end])

    cnt = 0
    q.append(end)
    visited = [False] * (n+1)
    while q:
        now = q.popleft()

        for time, before in graph2[now]:
            if times[now] - times[before] == time:
                cnt += 1
                if not visited[before]:
                    q.append(before)
                    visited[before] = True

    print(cnt)


n = int(input())
m = int(input())

graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

indegree = [0] * (n+1)

for _ in range(m):
    s, e, t = map(int, input().split())
    graph1[s].append((t, e))
    graph2[e].append((t, s))
    indegree[e] += 1

start, end = map(int, input().split())

topology_sort()
