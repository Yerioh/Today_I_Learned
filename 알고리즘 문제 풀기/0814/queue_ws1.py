import sys

sys.stdin = open("txt/in_ws1.txt", "r")


# 시작 노드 -> 도착 노드 간선의 수 계산
def bfs(arr, s, g, n):  # 인접 행렬, 시작노드, 도착노드, 노드 수 + 1
    visited = [0] * n
    q = [0] * n
    front = rear = 0
    v = s  # 현재 위치는 시작점
    # 시작점 enqueue
    q[rear] = v
    visited[v] = 1
    rear = (rear + 1) % n
    while front != rear:
        # dequeue
        t = q[front]
        front = (front + 1) % n
        # 도착점이라면
        if t == g:
            return visited[t] - 1  # 간선의 수는 시작점에서 도착점까지 가는 노드 수 - 1
        for i in range(1, n):
            # 인접한 노드이면서 방문하지 않았으면 enqueue
            if arr[t][i] == 1 and visited[i] == 0:
                q[rear] = i
                rear = (rear + 1) % n
                visited[i] = visited[t] + 1  # 시작점에서 이동한 횟수를 알기 위해
    return 0


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 노드의 개수, 간선의 개수
    adj_m = [[0] * (V + 1) for _ in range(V + 1)]  # 0 ~ V 까지 인덱스로 설정 (0은 안씀)
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_m[v1][v2] = 1
        adj_m[v2][v1] = 1
    S, G = map(int, input().split())  # 시작 노드, 도착 노드
    answer = bfs(adj_m, S, G, V + 1)
    print(f"#{tc} {answer}")
