import sys

sys.stdin = open('input_ws2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # 10*10 격자
    arr_10 = [[0] * 10 for _ in range(10)]
    # 칠할 영역의 수 N
    N = int(input())
    # N번 을 어떻게 칠할 것인가
    paint_list = [list(map(int, input().split())) for _ in range(N)]
    for paint in paint_list:
        for i in range(paint[0], paint[2] + 1):
            for j in range(paint[1], paint[3] + 1):
                # 빨간색으로 칠할 때
                if paint[4] == 1:
                    arr_10[i][j] += paint[4]
                # 파란색으로 칠할 때
                else:
                    arr_10[i][j] += paint[4]
    count_purple = 0
    for i in range(10):
        for j in range(10):
            if arr_10[i][j] == 3:
                count_purple += 1
    print(f'#{tc} {count_purple}')
