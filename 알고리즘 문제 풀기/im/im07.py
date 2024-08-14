import sys

sys.stdin = open("txt/in07.txt", "r")


# 오셀로 규칙에 따른 돌 뒤집기 시행
def othello(arr, r, c, p):
    arr[r][c] = p
    # 각 방향 검사
    dl = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    for dr, dc in dl:
        stack = []  # 상대 돌 저장
        vr, vc = r, c
        while True:
            nr, nc = vr + dr, vc + dc
            # 종료조건 1: 인덱스 범위 확인, 다음 돌이 빈공간이면
            if not(0 <= nr < len(arr)) or not(0 <= nc < len(arr)) or arr[nr][nc] == 0:
                break
            # 내 돌을 만나면
            if arr[nr][nc] == p:
                for i, j in stack:
                    arr[i][j] = p
                break
            # 종료가 되지 않았다면
            vr, vc = nr, nc
            stack.append((vr, vc))
    return arr


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 보드의 크기, 돌을 놓는 횟수
    # 게임을 시작했을 때의 보드
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2  # 백돌
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1  # 흑돌
    for _ in range(M):
        col, row, piece = map(int, input().split())
        board = othello(board, row - 1, col - 1, piece)
    # 흑돌, 백돌 계산
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            if board[i][j] == 2:
                white += 1
    print(f"#{tc} {black} {white}")
