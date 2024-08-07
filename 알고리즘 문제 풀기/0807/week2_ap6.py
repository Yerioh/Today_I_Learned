import sys

sys.stdin = open('txt/input_ap6.txt', 'r')

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
        # 방향  상       하     좌       우
        d1 = [(-1, 0), (1, 0), (-1, 0), (1, 0)]
        # 대각선 좌상     우상      좌하      우하
        d2 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    print(*board, sep='\n')
    # print(f'#{tc} {arr}')
