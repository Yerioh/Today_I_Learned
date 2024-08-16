import sys

sys.stdin = open("txt/in_ws4.txt", "r")


def othello(arr, r, c, p):  # 현재 보드, 행, 열, 플레이어
    # 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
    dl = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    n = len(arr)
    arr[r][c] = p  # 본인돌 놓기
    for dr, dc in dl:
        d = 0
        stack = []
        while True:
            d += 1
            nr, nc = r + dr * d, c + dc * d
            if 0 <= nr < n and 0 <= nc < n:  # 인덱스 범위 확인
                if arr[nr][nc] == p:  # 본인 돌과 만나면
                    while stack:  # 스택 안에 있는 칸을 전부 본인 돌로
                        vr, vc = stack.pop()
                        arr[vr][vc] = p
                    break
                elif arr[nr][nc] == 0:  # 빈칸과 만나면
                    break
                else:  # 상대 돌이라면
                    stack.append((nr, nc))
            else:  # 인덱스 벗어나면
                break
    return arr


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 보드의 크기, 돌을 놓는 횟수
    # 시작할 때의 보드, 1: 흑돌, 2: 백돌
    board = [[0] * N for _ in range(N)]
    board[N // 2][N // 2] = board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1
    for _ in range(M):
        col, row, player = map(int, input().split())  # 돌을 넣는 위치(r, c), 놓는 플레이어
        board = othello(board, row - 1, col - 1, player)
    # 정답 찾기
    black = white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            if board[i][j] == 2:
                white += 1
    print(f"#{tc} {black} {white}")
