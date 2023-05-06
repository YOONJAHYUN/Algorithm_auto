# 매개변수 탐색

def solution(stones, k):
    start = 0
    end = 200000000

    while start <= end:

        mid = (start + end) // 2

        count = 0
        for stone in stones:
            # 건너갈 수 있음 초기화
            if stone - mid > 0:
                count = 0
            # 건너 갈 수 없음
            else:
                count += 1
                # k개 넘을 경우 break
                if count >= k:
                    break

        # count 가 k보다 클 경우
        if count >= k:
            # mid를 줄여야됨
            end = mid -1
        else:
            start = mid + 1

    return start
