from collections import deque

def solution(maps):
    answer = -1
    
    n = len(maps)
    m = len(maps[0])
    q = deque()
    
    visited = [[0]*m for _ in range(n)]
    q. append((0,0))
    visited[0][0] = 1
    
    while q:
        
        y, x = q.popleft()
        if y == n-1 and x == m-1:
            answer = visited[y][x]
            break
        
        
        for dy, dx in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            ny, nx = y + dy, x + dx
            
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
    
    return answer