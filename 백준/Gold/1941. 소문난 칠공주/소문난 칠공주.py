import sys
from collections import deque
input = sys.stdin.readline

# 문어박사님 임포트함....

def bfs(si, sj):
    q = deque()
    vv = [[0]*5 for _ in range(5)]

    q.append((si, sj))
    vv[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < 5 and 0 <= nj < 5 and vv[ni][nj] == 0 and v[ni][nj] == 1:
                q.append((ni, nj))
                vv[ni][nj] = 1
                cnt += 1
    return cnt == 7


def check():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i, j)


# 가능한 조합을 모두 구한거임
def dfs(n, cnt, scnt):
    global ans

    if cnt > 7:
        return

    if n == 25:
        # 인접했는지 확인
        if cnt == 7 and scnt >= 4:
            if check():
                ans += 1
        return

    # 포함하는 경우
    v[n//5][n%5] = 1
    dfs(n+1, cnt+1, scnt+int(data[n//5][n%5]=='S'))
    # 포함하지 않는 경우
    v[n//5][n%5] = 0
    dfs(n+1, cnt, scnt)

data = [list(input().rstrip()) for _ in range(5)]
ans = 0
v = [[0]*5 for _ in range(5)]

dfs(0,0,0)
print(ans)
