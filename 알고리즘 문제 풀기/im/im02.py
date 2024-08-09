import sys

sys.stdin = open('txt/in02.txt', 'r')


def check_omok(r, c, n):
    row_check = 1
    col_check = 1
    cross_check1 = 1
    cross_check2 = 1
    for i in range(1, 3):
        left, right = c - i, c + i
        up, down = r - i, r + i
        # 행 체크
        if not (0 <= left < n) or arr[r][left] == '.':
            row_check = 0
        if not (0 <= right < n) or arr[r][right] == '.':
            row_check = 0
        # 열 체크
        if not (0 <= up < n) or arr[up][c] == '.':
            col_check = 0
        if not (0 <= down < n) or arr[down][c] == '.':
            col_check = 0
        # 좌우 대각선 체크
        if not (0 <= up < n and 0 <= left < n) or arr[up][left] == '.':
            cross_check1 = 0
        if not (0 <= down < n and 0 <= right < n) or arr[down][right] == '.':
            cross_check1 = 0
        # 우좌 대각선 체크
        if not (0 <= up < n and 0 <= right < n) or arr[up][right] == '.':
            cross_check2 = 0
        if not (0 <= down < n and 0 <= left < n) or arr[down][left] == '.':
            cross_check2 = 0
    # 하나라도 통과 됐다면
    if row_check or col_check or cross_check1 or cross_check2:
        return True
    return False


# 오목 판정
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기 N
    arr = [list(input()) for _ in range(N)]  # 돌 위치 배열
    answer = 'NO'
    for i in range(N):
        for j in range(N):
            # 현재 위치에 돌이 놓여있고 오목이 확인되었으면
            if arr[i][j] == 'o' and check_omok(i, j, N):
                answer = 'YES'
                break
        # 오목이 확인되었으면
        if answer == 'YES':
            break
    print(f'#{tc} {answer}')
