T = int(input())  # 테스트 케이스의 수


def n_queen(r, n):
    global answer
    # 종료조건 : 남은 퀸의 개수가 0이고, 마지막 행이면
    if n == 0 and r == N:
        answer += 1
        return
        #
    for c in range(N):
        check_place = True
        # 자신의 위에 퀸이 있나 확인
        for i in range(r):
            if board[i][c] == 1:
                check_place = False
                break
        for i in range(1, r + 1):
            # 인덱스 확인, 좌상으로 퀸이 있나 확인
            if r - i >= 0 and c - i >= 0 and board[r - i][c - i] == 1:
                check_place = False
                break
            # 인덱스 확인, 우상으로 퀸이 있나 확인
            if r - i >= 0 and c + i < N and board[r - i][c + i] == 1:
                check_place = False
                break
        # 퀸을 놓을수 있다면 다음 행으로 진행
        if check_place:
            board[r][c] = 1
            n_queen(r + 1, n - 1)
            # 위의 상황이 끝나면 원상복귀
            board[r][c] = 0


for tc in range(1, T + 1):
    N = int(input())  # 체스판의 크기, 놓아야 할 퀸의 수 N
    board = [[0] * N for _ in range(N)]  # 크기 N의 체스판
    answer = 0
    n_queen(0, N)
    print(f'#{tc} {answer}')
