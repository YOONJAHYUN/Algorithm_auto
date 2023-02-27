# 예진 코드

K = int(input())
max_height = 0 
max_width = 0  
max_width_index = 0 
max_height_index = 0 
info = []  

for i in range(6):
    tmp = list(map(int, input().split()))
    info.append(tmp)
    if tmp[0] == 1 or tmp[0] == 2:  
        if max_width < tmp[1]:  
            max_width = tmp[1]  
            max_width_index = i 
    else:
        if max_height < tmp[1]: 
            max_height = tmp[1] 
            max_height_index = i  


index_list = [info[max_height_index - 1], info[(max_height_index + 1) % 6], info[max_width_index - 1],
              info[(max_width_index + 1) % 6]]

p = 1  
for i in info: 
    if i not in index_list: 
        p *= i[1] 


result = (max_width * max_height - p) * K  
print(result)
