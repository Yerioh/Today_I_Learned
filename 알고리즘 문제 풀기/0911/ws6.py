# 보급로
import sys

sys.stdin = open("txt/in_ws6.txt", "r")

import heapq

dl = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 델타배열


def dijkstra(sr, sc):
    pq = []
    heapq.heappush(pq, (0, sr, sc))
    times[sr][sc] = 0
    while pq:
        t, vr, vc = heapq.heappop(pq)
        for dr, dc in dl:  # 상하좌우 순회
            nr, nc = vr + dr, vc + dc
            # 인덱스 확인
            if 0 <= nr < N and 0 <= nc < N:
                new_t = t + maps[nr][nc]
                # 새 시간이 현재 결정되어있는 값 이상이라면
                if new_t >= times[nr][nc]:
                    continue
                times[nr][nc] = new_t
                heapq.heappush(pq, (new_t, nr, nc))


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 지도의 크기
    maps = [list(map(int, input())) for _ in range(N)]  # 지도 정보
    # 시작점에서 각 좌표까지 걸리는 시간
    INF = int(1e9)
    times = [[INF] * N for _ in range(N)]
    dijkstra(0, 0)
    answer = times[N - 1][N - 1]
    print(f"#{tc} {answer}")
