# 최소 이동 거리
import sys

sys.stdin = open("txt/in_ws1.txt", "r")


def dfs(node, weight):
    global answer
    if weight >= answer:  # 현재 가중치가 지금 답 이상이면
        return
    if node == N:  # 마지막 노드에 도착했다면
        answer = weight
        return
    for next_node in range(N + 1):
        if adj_m[node][next_node]:  # 이동이 가능하다면 가중치를 늘려 재귀
            dfs(next_node, weight + adj_m[node][next_node])


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, E = map(int, input().split())  # 노드의 수, 간선의 수
    adj_m = [[0] * (N + 1) for _ in range(N + 1)]  # 가중치까지 쉽게 저장하기 위해 인접 행렬 사용
    for _ in range(E):
        x, y, w = map(int, input().split())  # x -> y, 가중치
        adj_m[x][y] = w
    answer = int(1e9)
    dfs(0, 0)
    print(f"#{tc} {answer}")
