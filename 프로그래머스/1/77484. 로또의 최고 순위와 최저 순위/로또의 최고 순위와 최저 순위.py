def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    win_nums.sort()
    
    LOTTO = [6, 6, 5, 4, 3, 2, 1]
    check = [False for _ in range(6)]
    
    '''
    지금 현재 중복된 숫자를 찾는다. 그럼 최저 등수가 나옴.
    미지수에 값을 넣으면서 최고값을 구한다.
    '''
    
    mini = 0
    x = 0
    for lotto in lottos:
        if lotto == 0:
            x += 1
        for i in range(6):
            win_num = win_nums[i]
            if lotto == win_num:
                mini += 1
                check[i] = True
                
    # print(check)
    # print(x)
    answer = [LOTTO[mini+x], LOTTO[mini]]
    # print(LOTTO[mini+x])
    
    # print(LOTTO[mini])
    
    return answer