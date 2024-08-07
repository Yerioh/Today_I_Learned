import sys

sys.stdin = open('txt/input_ap6.txt', 'r')


def is_vaild(r, c, n):  # 인덱스 검증
    return 0 <= r < n and 0 <= c < n

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 한 변의 길이 N, 돌을 놓는 횟수 M
    board = [[0] * N for _ in range(N)]
    board[N//2 - 1][N//2 - 1], board[N//2][N//2] = 2, 2
    board[N//2 - 1][N//2], board[N//2][N//2 - 1] = 1, 1
    # 돌을 놓는 순서 배열
    arr = [list(map(int, input().split())) for _ in range(M)]
    # 배열에서 열, 행, 돌의 종류 꺼내기
    for c, r, s in arr:
        c, r = c - 1, r - 1  # 인덱스에 맞춰서 변형
        board[r][c] = s
        #     상 하 좌 우 좌상 우상 좌하 우하 
        dr = [-1, 1, 0, 0, -1, -1, 1, 1]
        dc = [0, 0, -1, 1, -1, 1, -1, 1]
        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            lst = []  # 상대 돌 저장
            while True:
                # 인덱스를 벗어나거나 빈 공간이면 스택 초기화
                if not is_vaild(nr, nc, N) or board[nr][nc] == 0:
                    lst = []
                    break
                # 상대 돌 저장
                elif board[nr][nc] != s:
                    lst.append((nr, nc))
                # 본인 돌 만나면 break
                elif board[nr][nc] == s:
                    break
                nr, nc = nr + dr[d], nc + dc[d]
            # 저장된 상대 돌 변경
            for i, j in lst:
                board[i][j] = s
    # 흑돌, 백돌 검사
    black, white = 0, 0
    for row in board:
        for item in row:
            if item == 1:
                black += 1
            elif item == 2:
                white += 1
    print(f'#{tc} {black} {white}')
