import sys

input = sys.stdin.readline

n = int(input())
'''
curve
0 : 0
1 : 0 1
2 : 0 1 2 1
3 : 0 1 2 1 2 3 2 1
4 : 0 1 2 1 2 3 2 1 2 3 ...

'''
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

data = [[0] * 101 for _ in range(101)]


for _ in range(n):
    x, y, d, g = map(int, input().split())
    data[x][y] = 1

    move = [d]
    for i in range(g):
        tmp = []
        for j in range(len(move)-1, -1, -1):
            tmp.append((move[j]+1) % 4)
        move.extend(tmp)

    for k in move:
        nx = x + dx[k]
        ny = y + dy[k]
        data[nx][ny] = 1
        x, y = nx, ny


ans = 0
for i in range(101):
    for j in range(101):
       if data[i][j] == 1:
            temp = 1
            for di, dj in ((1, 0), (0, 1), (1,1)):
               ni, nj = i+di, j+dj
               if 0 <= ni < 101 and 0 <= nj < 101 and data[ni][nj] == 1:
                   temp += 1

            if temp == 4:
                ans += 1


print(ans)
