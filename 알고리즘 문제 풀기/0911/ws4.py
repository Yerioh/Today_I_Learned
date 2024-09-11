# 인수의 생일 파티
import sys

sys.stdin = open("txt/in_ws4.txt", "r")

import heapq


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start][start] = 0
    while pq:
        cost, now = heapq.heappop(pq)
        if cost < distance[start][now]:  # 이미 처리된 노드
            continue
        for n in adj_l[now]:
            next_node = n[0]
            new_cost = cost + n[1]
            if new_cost >= distance[start][next_node]:  # 값이 작아지지 않으면 skip
                continue
            distance[start][next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))
    return distance[X]  # 인수 집까지의 가중치


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())  # 노드의 수, 간선의 수, 인수의 집
    adj_l = [[] for _ in range(N + 1)]  # 그래프 정보를 담을 인접 리스트
    for _ in range(M):
        x, y, w = map(int, input().split())  # x -> y, 가중치
        adj_l[x].append((y, w))  # 유향 그래프이기 때문에 한 방향으로만 적용
    answer = 0  # 가장 오래 걸리는 시간
    INF = int(1e9)
    distance = [[INF] * (N + 1) for _ in range(N + 1)]  # 각 집에서 각 집까지 걸리는 시간
    for i in range(1, N + 1):
        dijkstra(i)
    for x in range(1, N + 1):
        time = distance[x][X] + distance[X][x]  # 각 집에서 인수집까지 왕복하는 시간
        answer = max(time, answer)
    print(f"#{tc} {answer}")
