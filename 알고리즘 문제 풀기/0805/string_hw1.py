import sys

sys.stdin = open('txt/input_hw1.txt', 'r')

T = 10
for tc in range(1, T + 1):
    N = int(input())  # 찾아야 할 회문의 길이
    arr = [list(input()) for _ in range(8)]
    answer = 0
    # 행 순회 회문 체크
    for i in range(8):
        for j in range(8 - N + 1):
            check_row = True
            for k in range(N//2):
                # 행 회문 체크
                if arr[i][j + k] != arr[i][j + N - 1 - k]:
                    check_row = False
            if check_row:
                answer += 1
    # 열 순회 회문 체크
    for i in range(8):
        for j in range(8 - N + 1):
            check_col = True
            for k in range(N//2):
                # 행 회문 체크
                if arr[j + k][i] != arr[j + N - 1 - k][i]:
                    check_col = False
            if check_col:
                answer += 1
    print(f'#{tc} {answer}')
