import sys

sys.stdin = open("txt/in_14413.txt", "r")


def check_fill(arr):
    dl = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    for r in range(N):
        for c in range(M):
            if arr[r][c] != "?":  # 색이 정해져 있는 곳일 때
                op = "." if arr[r][c] == "#" else "#"
                for dr, dc in dl:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M:  # 인덱스 범위 확인
                        if arr[nr][nc] == "?":  # ? 면 반대색 색칠
                            arr[nr][nc] = op
                        elif arr[nr][nc] == arr[r][c]:  # 같은 색이면 불가능
                            return "impossible"
    return "possible"


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열의 크기 N, M
    board = [list(input()) for _ in range(N)]
    answer = check_fill(board)
    print(f"#{tc} {answer}")
