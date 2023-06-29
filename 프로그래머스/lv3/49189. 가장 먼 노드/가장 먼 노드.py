from collections import deque, Counter

def solution(n, edge):
    answer = 0
    def BFS(node):
        q = deque()
        v = [False] * (n+1)
        q.append((node, 1))
        v[node] = True
        check = [0] * (n+1)
        check[node] = 1
        
        while q:
            
            now, cnt = q.popleft()
            
            for next in graph[now]:
                if not v[next]:
                    v[next] = True
                    q.append((next, cnt+1))
                    check[next] = cnt+1
        
        counter =Counter(check)
        my_max = max(counter)
        print(counter[my_max])
        return counter[my_max]
        
                    
            
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    # print(graph)
    
    answer = BFS(1)
    return answer