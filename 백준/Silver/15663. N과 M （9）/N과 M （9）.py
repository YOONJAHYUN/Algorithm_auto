import sys

input = sys.stdin.readline

def NM(depth, i):

    if depth == M:
        result = i.lstrip()
        print(result)
        return
    prev = 0
    for j in range(0, N):
        if not selection[j] and prev != numbers[j]:
            prev = numbers[j]

            selection[j] = True
            NM(depth+1, i + ' ' + str(numbers[j]))
            selection[j] = False

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()
selection= [False] * N
NM(0, '')
