import sys

sys.stdin = open('input_ws4.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    # 배열의 크기 N, 파리채의 크기 M
    N, M = map(int, input().split())
    # 파리 배열
    flies = [list(map(int, input().split())) for _ in range(N)]
    # 파리를 찾기 위한 델타 배열
    delta_list = []
    for i in range(M):
        for j in range(M):
            delta_list.append([i, j])
    # 파리 찾기
    max_fly = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_sum = 0
            for d in delta_list:
                ni = i + d[0]
                nj = j + d[1]
                fly_sum += flies[ni][nj]
            if fly_sum > max_fly:
                max_fly = fly_sum
    print(f'#{tc} {max_fly}')
