import sys

sys.stdin = open("txt/in_maze.txt", "r")


# 인덱스 검사
def is_valid(r, c, n):
    return 0 <= r < n and 0 <= c < n


# 미로까지의 최소거리 찾기
def maze_bfs(arr, n, v):  # 탐색할 2차원 배열, 배열의 크기, 시작점
    visited = [[0] * n for _ in range(n)]  # 2차원 배열의 각 원소를 방문했는지 확인
    q = [0] * (n ** 2)
    front = rear = 0
    sr, sc = v  # 시작점
    # enqueue
    q[0] = v
    visited[sr][sc] = 1
    rear = (rear + 1) % (n ** 2)
    # 상하좌우 확인 위한 델타 배열
    dl = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while front != rear:
        # dequeue
        vr, vc = q[front]
        front = (front + 1) % (n ** 2)
        if arr[vr][vc] == 3:  # 출구라면
            return visited[vr][vc] - 2  # 시작점과 출구는 계산에서 제외
        for dr, dc in dl:
            nr, nc = vr + dr, vc + dc
            # 인덱스 범위 검사, 해당 칸이 통로, 방문한적 없음
            if is_valid(nr, nc, n) and arr[nr][nc] != 1 and visited[nr][nc] == 0:
                q[rear] = [nr, nc]
                rear = (rear + 1) % (n ** 2)
                visited[nr][nc] = visited[vr][vc] + 1
    return 0


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 미로의 크기 N
    maze = [list(map(int, input())) for _ in range(N)]  # N 크기의 미로의 모양
    # 시작점 찾기
    start = [0, 0]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
    answer = maze_bfs(maze, N, start)
    print(f"#{tc} {answer}")
