from collections import deque
 

def solution(queue1, queue2):
    answer = 0
    n = len(queue1)
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    numbers = queue1 + queue2
    # numbers.sort()
    # my_max = numbers[-1]
    my_sum = sum(numbers)
    
    if my_sum % 2:
        answer = -1

    else:
        sum1 = sum(q1)
        sum2 = sum(q2)
        while answer <= n*4:
            
            
            if sum1 > sum2:
                num1 = q1.popleft()
                q2.append(num1)
                answer +=1
                sum1 -= num1
                sum2 += num1
                
            elif sum1 == sum2:
                break

            else:
                num2 = q2.popleft()
                q1.append(num2)
                answer += 1
                sum1 += num2
                sum2 -= num2
        else:
            answer = -1
                
    return answer