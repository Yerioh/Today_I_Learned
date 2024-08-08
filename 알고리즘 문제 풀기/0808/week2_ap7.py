import sys

sys.stdin = open('txt/input_ap7.txt', 'r')


# 손님 수, 붕어빵이 나오는 시간, 붕어빵이 나오는 개수, 손님의 방문 시간 리스트
def sail_bread(n, m, k, lst):
    bread = 0  # 현재 붕어빵의 개수
    time = 0  # 진행된 시간
    visited = [0] * n  # 붕어빵을 사간 것을 확인
    while n > 0:
        time += m
        cnt = 0  # 이번 타임에 방문한 손님의 수
        for i in range(len(lst)):
            if not visited[i] and lst[i] < time:  # 방문한 적이 없는 손님이 도착했다면
                if bread:  # 붕어빵이 있다면
                    bread -= 1  # 붕어빵 -1
                    visited[i] = 1
                    cnt += 1
                else:  # 붕어빵이 없다면
                    return 'Impossible'
        n -= cnt  # 남은 손님 수
        bread += k  # 다음 타임에 팔 붕어빵
    return 'Possible'


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    # 손님의 수, M초의 시간 동안 K개의 붕어빵
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))  # 각 손님이 도착하는 초
    print(f'#{tc} {sail_bread(N, M, K, arr)}')
