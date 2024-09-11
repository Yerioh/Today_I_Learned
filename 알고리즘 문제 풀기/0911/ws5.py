# 하나로
import sys

sys.stdin = open("txt/in_ws5.txt", "r")

import math


def find_set(x):  # 집합의 대표자 찾기 + 경로 압축
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union_set(x, y):  # 집합 합치기
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x == root_y:
        return
    if root_x < root_y:
        p[root_y] = root_x
    else:
        p[root_x] = root_y


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 섬의 개수
    island = [list(map(int, input().split())) for _ in range(2)]  # 각 섬의 좌표
    E = float(input())  # 환경 부담 세율
    distance = []  # 각 섬에서 다른 섬까지의 거리
    for i in range(N - 1):
        for j in range(i + 1, N):
            d = math.sqrt(abs(island[0][i] - island[0][j]) ** 2 + abs(island[1][i] - island[1][j]) ** 2)
            distance.append((i, j, d))
    distance.sort(key=lambda x: x[2])
    p = [i for i in range(N)]  # 각 노드의 부모 노드 표시
    cnt = 0
    answer = 0
    for v1, v2, dist in distance:
        if find_set(v1) != find_set(v2):
            union_set(v1, v2)
            cnt += 1
            answer += dist ** 2 * E
            if cnt == N + 1:
                break
    print(f"#{tc} {round(answer)}")
