def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    x = n-1
    
    cnt = 0
    my_max = citations[x]
    
    while True:
        
        for citation in citations[::-1]:
            if citation >= my_max:
                cnt += 1
            else:
                break
                
        if cnt >= my_max and (n-cnt) <= my_max:
            answer = my_max
            break
        else:
            my_max -= 1
            cnt = 0
                    
    
                    
    return answer