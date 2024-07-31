import sys

sys.stdin = open('input_ws4.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T+1):
    # 배열의 크기 N, 파리채의 크기 M
    N, M = map(int, input().split())
    # 파리 배열
    flies = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_sum = 0
            for k in range(M):
                fly_sum = flies[i][j] + flies[i][j+1] + flies[i][]
