from collections import deque
import sys
sys.setrecursionlimit(10**6)
result = 0
def solution(maps):
    w = len(maps[0])
    h = len(maps)
    
    
    start = ()
    lever = ()
    finish = ()
    # 1 시작 지점 찾기
    # 2 레버 찾기
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                start = (i,j)
            if maps[i][j] == 'L':
                lever = (i,j)
            if maps[i][j] == 'E':
                finish = (i,j)
            if start and lever and finish:
                break
                
    # bfs로 가장 빠르게 가는 길 찾기
    bfs(start, lever, w, h, maps)
    # print(start, lever, n)
    if result != -1:
        bfs(lever, finish, w, h, maps)
        
    answer = result
    return answer

def bfs(start, end, w, h, maps):
    global result
    
    visited = [[False]*w for _ in range(h)]
    si, sj = start
    ei, ej = end
    visited[si][sj] = True
    # print(start, end)    
    q = deque()
    q.append((si,sj,0))
    # print(q)
    while q:
        si, sj, cnt = q.popleft()
        # if si == ei and sj == ej:
        #     result += cnt
        #     return
        
        for di, dj in ((1,0), (-1, 0), (0,1), (0, -1)):
            ni, nj = si+di, sj+dj
            if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and maps[ni][nj] != 'X':
                visited[ni][nj] = True
                if ni == ei and nj == ej:
                    result += cnt +1
                    return
                else:
                    q.append((ni, nj, cnt+1))
    else:
        
        result = -1
        return     