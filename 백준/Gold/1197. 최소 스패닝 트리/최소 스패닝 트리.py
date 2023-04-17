import sys
input = sys.stdin.readline

def find(start):
    if start != vroot[start]:
        vroot[start] = find(vroot[start])
    return vroot[start]

V, E = map(int, input().split())
graph = []

for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()
vroot = [i for i in range(V+1)]
ans = 0
# union 과정
for cost, a, b in graph:
    aa = find(a)
    bb = find(b)

    # 순환하지 않는다는 의미
    if aa != bb:
        if aa > bb:
            vroot[aa] = bb
        else:
            vroot[bb] = aa
        ans += cost
print(ans)
