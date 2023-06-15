from collections import deque

def solution(n, computers):
    answer = 0
    v = [False] * n
    
    def BFS(s):
        v[s] = True
        q = deque()
        q.append(s)
        
        while q:
            now = q.popleft()
            for i in range(n):
                if computers[now][i] == 1 and not v[i]:
                    v[i] = True
                    q.append(i)
                    
    for i in range(n):
        if not v[i]:
            BFS(i)
            answer += 1
        
    return answer