# 쿼드 트리
import sys

input = sys.stdin.readline

def zero_one_zip(x, y, n):
    cnt0 = 0
    cnt1 = 0

    for i in range(x, x+n):
        for j in range(y, y+n):
            if data[i][j] == 0:
                cnt0 += 1
            else:
                cnt1 += 1

    if cnt0 == n**2:
        print(0, end='')
    elif cnt1 == n**2:
        print(1, end='')
    else:
        print('(', end='')
        zero_one_zip(x, y, n//2)
        zero_one_zip(x, y+n//2, n//2)

        zero_one_zip(x+n//2, y, n//2)
        zero_one_zip(x+n//2, y+n//2,n//2)
        print(')', end='')



N = int(input())

data = [list(map(int, input().rstrip())) for _ in range(N)]

zero_one_zip(0, 0, N)

