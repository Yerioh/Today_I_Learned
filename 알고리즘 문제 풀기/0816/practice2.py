import sys

sys.stdin = open("txt/in_pr2.txt", "r")


def check_color(arr, n, m, s):
    visited = [[0] * m for _ in range(n)]
    qsize = n * m
    q = [[0, 0]] * qsize
    front = rear = 0
    sr, sc = s  # 시작 위치
    print(sr, sc)
    q[rear] = [sr, sc]
    visited[sr][sc] = 1
    rear = (rear + 1) % qsize
    dl = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우
    while front != rear:
        r, c = q[front]
        front = (front + 1) % qsize
        op = "." if arr[r][c] == "#" else "#"  # 상대 색
        for dr, dc in dl:  # 인접칸 확인
            nr, nc = r + dr, c + dc
            # 인덱스 범위 확인, 방문 확인
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if arr[nr][nc] == arr[r][c]:  # 자신과 같은 색이라면
                    for a in arr:
                        print(a)
                    return "impossible"
                elif arr[nr][nc] == "?":  # 색이 정해지지 않았다면
                    arr[nr][nc] = op
                q[rear] = [nr, nc]
                visited[nr][nc] = 1
                rear = (rear + 1) % qsize
    for a in arr:
        print(a)
    return "possible"


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 격자판의 크기
    A = [list(input()) for _ in range(N)]  # 격자판 배열
    S = [-1, -1]
    for i in range(N):
        for j in range(M):
            if A[i][j] != "?":
                S = [i, j]
                break
        if S != [-1, -1]:
            break
    print(S)
    answer = check_color(A, N, M, S)
    print(f"#{tc} {answer}")
