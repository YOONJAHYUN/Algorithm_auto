

T = int(input())

for tc in range(1, T+1):
    clap = list(map(int, input().rstrip()))
    
    clapclap = []
    clapclap.append(clap[0])
    # i번째 글자는, 박수하고 있는 사람이 i-1 명 이상일 때 박수치는 사람을 의미한다.
    # 인덱스는 0번부터 시작하므로, i-1번째 글자는 인덱스 i보다 많은 사람이 박수를 치고 있어야함을 의미한다.
    # 누적을 하면서 인덱스 값보다 큰지 판단하고, 크지 않다면 모자란만큼 값을 더해준다.
    # 그 값을 count
    cnt = 0
    for i in range(1,len(clap)):
        clapclap.append(clap[i] + clapclap[i-1])
        if clapclap[i-1] < i:
            cnt += i - clapclap[i-1]
            clapclap[-1] += i - clapclap[i-1]

    
    print(f'#{tc}',cnt)
