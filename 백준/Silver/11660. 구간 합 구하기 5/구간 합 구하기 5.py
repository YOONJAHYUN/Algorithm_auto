import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(1, N):
        data[i][j] += data[i][j-1]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    my_sum = 0
    # 합부터 구하기
    for i in range(x1-1, x2):
        if 0 <= i < N:

            my_sum += data[i][y2-1]
            if 0 <= y1 - 2 < N:
                my_sum -= data[i][y1-2]
 
    print(my_sum)
    