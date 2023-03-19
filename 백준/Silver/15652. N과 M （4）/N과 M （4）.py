import sys

input = sys.stdin.readline

def NM(depth, i, idx):
    if depth == M:
        print(i.lstrip())
        return

    for j in range(idx, N+1):
        idx = j
        NM(depth+1, i + ' ' + str(j), idx)


N, M = map(int, input().split())

selection = [False] * (N+1)

NM(0, '', 1)

