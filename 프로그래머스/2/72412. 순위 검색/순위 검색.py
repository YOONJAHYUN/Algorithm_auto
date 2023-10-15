from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    dict = {}
    
    for i in range(len(info)):

        candi = info[i].split(" ")
        
        candi_key = candi[:-1]
        candi_val = candi[-1]
        
        for j in range(5):
            for combi in combinations(candi_key, j):
                temp = ''.join(combi)
                
                if dict.get(temp):
                    dict[temp].append(int(candi_val))
                else:
                    dict[temp] = [int(candi_val)]
                    
    # print(dict)
    
    for d in dict:
        dict[d].sort()
    
    
    for q in query:
        temp = (q.replace(" and", "").replace("-", "").split(" "))
        # print(temp)
        temp_key = ''.join(temp[:-1])
        temp_val = int("".join(temp[-1]))
        cnt = 0
        if dict.get(temp_key):
            
            enter = bisect_left(dict[temp_key], temp_val)

            answer.append(len(dict[temp_key]) - enter)
        else:
            answer.append(0)
                          
                    
        
        
        

    return answer