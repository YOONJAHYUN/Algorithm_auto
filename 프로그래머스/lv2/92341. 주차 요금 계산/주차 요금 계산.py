import math
    
def solution(fees, records):
    answer = []
    # 기본 정보
    basic_min, basic_fee, unit_min, unit_money = fees
    
    print(basic_min, basic_fee, unit_min, unit_money)
    
    # 차량 정보
    n = len(records)
    print(n)
    cars = {}
    # 차량 번호 순으로 정렬
    records.sort(key=lambda x: x[6:10])
    
    # flag로 입출차 표기
    flag = 'IN'
    
    # 누적 시간 저장
    time = 0
    
    # 현재 조사하는 차량번호
    car_num = records[0][6:10]
    
    # 차량번호 모으기
    car_numbers = set()
    car_numbers.add(car_num)
    
    for i in range(n):
        # 차량번호 모으고 시작
        car_numbers.add(records[i][6:10])
        
        # 지금 조사하는 차량이 이전차량과 같다면
        if records[i][6:10] == car_num:
            # 출차되는 경우
            if records[i][11:] == 'OUT':
                time += int(records[i][0:2]) * 60
                time += int(records[i][3:5])
                flag = 'OUT'
                
            # 입차되는 경우
            else:
                time -= int(records[i][0:2]) * 60
                time -= int(records[i][3:5])
                flag = 'IN'
            # 근데 마지막 정보라면?
            if i == n-1:
                # 아직 출차가 안됐다?
                if flag =='IN':
                    # 마지막 타임을 더해준다
                    time += 23 * 60
                    time += 59
                    
                # 마지막 차량까지 시간을 더해준다. 
                cars[car_num] = time
        # 차 변경        
        else:
            # 근데 만약 아직 out되지 않았다면
            if flag =='IN':
                time += 23 * 60
                time += 59
            # 이전 값들 담고
            cars[car_num] = time
            # 차 번호 갱신
            car_num = records[i][6:10]
            flag = 'IN'
            
            # 시간 갱신
            time = 0
            time -= int(records[i][0:2]) * 60
            time -= int(records[i][3:5])
            if i == n-1:
                # 근데 만약 아직 out되지 않았다면
                if flag =='IN':
                    time += 23 * 60
                    time += 59
                cars[car_num] = time
                
                
    
    print(cars)
    print(car_numbers)
    car_numbers = list(car_numbers)
    car_numbers.sort()
    for number in car_numbers:
        res = 0
        # 기본 시간보다 작은경우
        if cars[number] <= basic_min:
            answer.append(basic_fee)
        # 큰경우
        else:
            # 기본요금 더하기
            res += basic_fee
            # 기본시간 뺀거
            time = cars[number] - basic_min
            print(time)
            print(math.ceil(time/unit_min))
            res += math.ceil(time/unit_min) * unit_money
            answer.append(res)
    
    return answer