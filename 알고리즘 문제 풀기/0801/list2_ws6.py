import sys

sys.stdin = open('txt/input_ws6.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열의 크기 N, M
    balloons = [list(map(int, input().split())) for _ in range(N)]
    # 상 하 좌 우 방향 -> 0 1 2 3
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_sum = 0
    # 풍선 배열 순회
    for i in range(N):
        for j in range(M):
            flower_sum = balloons[i][j]
            # 델타 배열 순회를 처음 터트린 풍선의 꽃가루 만큼
            for k in range(1, balloons[i][j] + 1):
                # 델타 배열 순회
                for idx in d:
                    ni = i + idx[0] * k
                    nj = j + idx[1] * k
                    if 0 <= ni < N and 0 <= nj < M:
                        flower_sum += balloons[ni][nj]
            if flower_sum > max_sum:
                max_sum = flower_sum
    print(f'#{tc} {max_sum}')
