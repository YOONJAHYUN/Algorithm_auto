def solution(s):
    answer = ''
    text = ''
    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six' : '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    
    for i in s:
        if i.isdigit() == True:
            if text:
                answer += numbers[text]
                text = ''
            answer += str(i)
                
        else:
            text += i
            if numbers.get(text):
                answer += numbers[text]
                text = ''
                
    return int(answer)