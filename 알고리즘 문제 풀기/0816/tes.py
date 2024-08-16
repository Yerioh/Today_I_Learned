import sys

sys.stdin = open("txt/in_pr2.txt", "r")


def check_color(arr, n, m):
    dl = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r in range(n):
        for c in range(m):
            if arr[r][c] != "?":  # 색을 칠할 칸이 정해져 있다면
                op = "." if arr[r][c] == "#" else "#"  # 상대 색
                for dr, dc in dl:  # 인접칸 확인
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m:  # 인덱스 범위 확인
                        if arr[nr][nc] == arr[r][c]:  # 자신과 같은 색이라면
                            return "impossible"
                        elif arr[nr][nc] == "?":  # 색이 정해지지 않았다면
                            arr[nr][nc] = op
    return "possible"


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 격자판의 크기
    A = [list(input()) for _ in range(N)]  # 격자판 배열
    answer = check_color(A, N, M)
    print(f"#{tc} {answer}")