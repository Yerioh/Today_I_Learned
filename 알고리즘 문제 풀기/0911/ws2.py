# 최소 비용
import sys

sys.stdin = open("txt/in_ws2.txt", "r")

import heapq

dl = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # 상하좌우 델타 배열


def dijkstra(sr, sc):
    pq = []
    heapq.heappush(pq, (0, sr, sc))  # 가중치, 좌표 순으로 저장
    distance[sr][sc] = 0
    while pq:
        d, vr, vc = heapq.heappop(pq)
        if distance[vr][vc] < d:
            continue
        for dr, dc in dl:
            nr, nc = vr + dr, vc + dc
            # 인덱스 확인
            if 0 <= nr < N and 0 <= nc < N:
                # 다음 지역이 현재 지역보다 높으면 그 차만큼 연료를 더 소비함
                h = maps[nr][nc] - maps[vr][vc] if maps[nr][nc] > maps[vr][vc] else 0
                new_cost = d + 1 + h
                if new_cost >= distance[nr][nc]:
                    continue
                distance[nr][nc] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc))


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 지도의 크기
    maps = [list(map(int, input().split())) for _ in range(N)]  # 지도의 정보
    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]
    dijkstra(0, 0)
    answer = distance[N - 1][N - 1]
    print(f"#{tc} {answer}")
