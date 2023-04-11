import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start):

    q = []

    heappush(q, start)

    while q:
        cost, now = heappop(q)
        

        if visited[now][0] < cost:
            continue

        for new_cost, new_location in graph[now]:
            res = new_cost + cost

            if res < visited[new_location][0]:
                visited[new_location][0] = res
                visited[new_location][1] = now
                # for dir in visited[now][1]:
                #     visited[new_location][1].append(dir)

                heappush(q,(res, new_location))


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [[int(1e9), 0] for _ in range(n+1)]
result = []

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

s, e = map(int, input().split())
visited[s][0] = 0

dijkstra((0, s))
end = e
while end != s:
    result.append(end)
    end = visited[end][1]

# 최소비용
print(visited[e][0])
print(len(result)+1)
print(s, *result[::-1])
