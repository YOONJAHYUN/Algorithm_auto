from itertools import combinations

def check(lst, n, orders):
    
    my_max = 0
    res = []
    for combi in lst:
        count = 0
        # print(combi)
        for order in orders:
            for char in combi:
                if char not in order:
                    break
            else:
                count += 1
                
        if count >= 2:
            if my_max < count: 
                my_max = count
                res = []
                res.append(''.join(sorted(combi)))
                
            elif my_max == count:
                
                temp = ''.join(sorted(combi))
                
                               
                if temp not in res:
                    res.append(temp)
    print(res)
    return res
    


def solution(orders, course):
    answer = []
    # print(orders)
    
    # dishes = set()
    # for dish in orders:
    #     for char in dish:
    #         dishes.add(char)
    # dishes = list(dishes)
    # dishes.sort()

    for num in course:
        dishes = set(combinations(orders[0], num))
        for i in range(len(orders)):
            dishes = dishes|set(combinations(orders[i], num))
        dishes = list(dishes)
        # print(dishes)
        
        # combis = list(combinations(dishes, num))
        # check(dishes, num, orders)
        for ans in check(dishes, num, orders):
            answer.append(ans)
                    
    answer.sort()
    return answer
        