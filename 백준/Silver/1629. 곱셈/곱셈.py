import sys
input = sys.stdin.readline
# 자연수 = 1 이상인 정수
A, B, C = map(int, input().split())

# 프로그램을 작성하시오 -> 함수를 만들어라?

def f(a, b, c):

    if b == 1:
        return a%c

    elif b == 2:
        return (a*a)%c

    else:

        if b%2: # 만약 홀수라면
            return ((f(a, (b-1)//2, c)**2)*a)%c
        else:   # 짝수라면
            return (f(a, b//2, c)**2)%c

print(f(A, B, C))