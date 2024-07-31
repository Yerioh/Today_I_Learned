import sys

sys.stdin = open('input_hw1.txt', 'r')

T = 10
for _ in range(1, T + 1):
    # tc = int(input())
    # arr_100 = [list(map(int, input().split())) for _ in range(100)]
    # max_sum = 0
    # # 행 비교하여 최대값 구하기
    # max_row = 0
    # for i in range(100):
    #     s1 = 0
    #     for j in range(100):
    #         s1 += arr_100[i][j]
    #     if s1 > max_row:
    #         max_row = s1
    # max_sum = max_row
    # # 열 비교하여 최대값 구하기
    # max_col = 0
    # for j in range(100):
    #     s2 = 0
    #     for i in range(100):
    #         s2 += arr_100[i][j]
    #     if s2 > max_col:
    #         max_col = s2
    # max_sum = max_col if max_col > max_sum else max_sum
    # # 최대 대각선 구하기
    # s3 = 0
    # s4 = 0
    # for i in range(100):
    #     s3 += arr_100[i][i]
    #     s4 += arr_100[i][-1 - i]
    # max_cross = s3 if s3 >= s4 else s4
    # max_sum = max_cross if max_cross > max_sum else max_sum
    # print(f'#{tc} {max_sum}')

    tc = int(input())
    arr_100 = [list(map(int, input().split())) for _ in range(100)]
    max_row = 0
    max_col = 0
    cross_sum1 = 0
    cross_sum2 = 0
    for i in range(100):
        s1 = 0
        s2 = 0
        for j in range(100):
            # 행의 합 구하기
            s1 += arr_100[i][j]
            # 열의 합 구하기
            s2 += arr_100[j][i]
            # 왼쪽부터 시작하는 대각선 합 구하기
            if j == i:
                cross_sum1 += arr_100[i][j]
            # 오른쪽부터 시작하는 대각선 합 구하기
            if j == 99 - i:
                cross_sum2 += arr_100[i][j]
        if s1 > max_row:
            max_row = s1
        if s2 > max_col:
            max_col = s2
    max_sum = max([max_row, max_col, cross_sum1, cross_sum2])
    print(f'#{tc} {max_sum}')
