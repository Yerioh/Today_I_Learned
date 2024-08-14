import sys

sys.stdin = open("txt/in_hw1.txt", "r")


# 인덱스 범위 확인
def is_valid(r, c, n):
    return 0 <= r < n and 0 <= c < n


# 출발점부터 도착지까지의 길 확인
def maze_bfs(maze, s):  # 탐색할 미로 배열, 시작점
    visited = [[0] * 16 for _ in range(16)]
    qsize = 16 ** 2
    q = [[0, 0]] * qsize
    front = rear = 0
    # 시작점 enQueue
    sr, sc = s
    q[rear] = [sr, sc]
    rear = (rear + 1) % qsize
    visited[sr][sc] = 1
    while front != rear:
        # deQueue
        vr, vc = q[front]
        front = (front + 1) % qsize
        # 도착점에 도착했다면 종료
        if maze[vr][vc] == 3:
            return 1
        # 상하좌우를 확인하여 이동 가능한지 확인
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = vr + dr, vc + dc
            # 인덱스 범위 안이고 이동 가능하고 방문한적 없으면 enQueue
            if is_valid(nr, nc, 16) and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                q[rear] = [nr, nc]
                rear = (rear + 1) % qsize
                visited[nr][nc] = visited[vr][vc] + 1
    # 도착점에 도착하지 못하고 탐색이 종료되었다면
    return 0


for _ in range(10):
    tc = "#" + input()  # 테스트 케이스의 번호
    arr = [list(map(int, input())) for _ in range(16)]  # 미로의 모양
    S = [0, 0]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                S[0], S[1] = i, j
    answer = maze_bfs(arr, S)
    print(tc, answer)
