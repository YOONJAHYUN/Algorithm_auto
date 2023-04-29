from itertools import permutations

def check(lst, ids, n):
    
    for i in range(n):
        # 길이가 같지않으면 안됨
        if len(lst[i]) != len(ids[i]):
            
            return
        
        for j in range(len(lst[i])):
            # *가 아닌데 단어가 같지않으면 안됨
            if ids[i][j] != '*' and lst[i][j] != ids[i][j]:
                return
            
    return sorted(lst)


def solution(user_id, banned_id):
    result = []
    m = len(banned_id)
    
    for combi in permutations(user_id, m):
        temp = check(combi, banned_id, m)
        if temp and temp not in result:
            print(temp)
            result.append(temp)
        
    answer = len(result)
    # print(result)
    return answer