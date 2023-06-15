from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        answer = 0
    else:
        n = len(begin)
        q = deque()
        q.append((begin, 0))
        
        while q:
            w, count = q.popleft()
            if w == target:
                answer = count
                break
            for word in words:
                cnt  = 0
                for i in range(n):
                    if w[i] != word[i]:
                        cnt += 1
                    if cnt > 1:
                        break
                if cnt == 1:
                    q.append((word, count +1))
        
        
        
    return answer