def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    the_end = 3000001
    
    # print(routes)
    
    for start, end in routes:
        # start, end = route
        if start <= the_end <= end:
            continue
        else:
            the_end = end
            answer += 1
        
    return answer