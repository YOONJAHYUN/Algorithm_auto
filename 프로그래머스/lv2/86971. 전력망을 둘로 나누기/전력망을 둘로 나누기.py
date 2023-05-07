from collections import deque

def bfs(s, e, n, node):
    
    visited = [False] * (n+1)
    visited[s] = True
    cnt = 1
    q = deque()
    for i in node[s]:
        if i != e:
            q.append(i)
            visited[i] = True
            cnt +=1
    while q:
        my_node = q.popleft()
        
        for i in node[my_node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
                
    return cnt
    
          
    

def solution(n, wires):
    answer = n

    node = [[] for _ in range(n+1)]
    for i in range(n-1):
        a, b = wires[i]

        node[a].append(b)
        node[b].append(a)
    # print(node)
    
    for s, e in wires:
        # s와 e 간선을 끊고 개수세기
        count = bfs(s, e, n, node)
        # print(count)
        new = n-count
        
        answer = min(answer, abs(new- count))
        
        
    return answer