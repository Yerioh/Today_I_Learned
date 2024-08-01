import sys

sys.stdin = open('txt/input_ws4.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # 배열의 크기 N, 단어의 길이 K
    N, K = map(int, input().split())
    # 퍼즐의 모양
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt_k = 0
    for i in range(N):
        check_row = 0
        check_col = 0
        for j in range(N):
            # 행 탐색
            if puzzle[i][j] == 0:
                # 이전까지 체크된 길이가 K라면
                if check_row == K:
                    cnt_k += 1
                check_row = 0
            else:
                check_row += 1
            # 열 탐색
            if puzzle[j][i] == 0:
                # 이전까지 체크된 길이가 K라면
                if check_col == K:
                    cnt_k += 1
                check_col = 0
            else:
                check_col += 1
        if check_row == K:
            cnt_k += 1
        if check_col == K:
            cnt_k += 1
    print(f'#{tc} {cnt_k}')
