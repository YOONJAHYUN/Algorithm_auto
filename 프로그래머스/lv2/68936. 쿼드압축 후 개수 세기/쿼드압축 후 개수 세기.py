      
def solution(arr):

    n = len(arr[0])
    
    Quadtree(0, 0, n, arr)
    
    
    answer = [result1, result2]
    
    return answer

result1 = 0
result2 = 0  

def Quadtree(y, x, n, arr):
    global result1, result2
    
    cnt1 = 0
    cnt2 = 0

    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[i][j] == 0:
                cnt1 += 1
            else:
                cnt2 += 1

                
    if cnt1 == n**2:
        result1 += 1
        return
    
    elif cnt2 == n**2:
        result2 += 1
        return

    else:
        Quadtree(y, x, n//2, arr)
        Quadtree(y+n//2, x, n//2, arr)
        Quadtree(y, x+n//2, n//2, arr)
        Quadtree(y+n//2, x+n//2, n//2, arr)