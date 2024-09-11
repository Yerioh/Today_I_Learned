# 최소 신장 트리
import sys

sys.stdin = open("txt/in_ws3.txt", "r")


def find_set(x):  # 집합의 대표자 찾기 + 경로 압축
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union_set(x, y):  # 집합 합치기
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 노드의 수, 간선의 수
    edge = [list(map(int, input().split())) for _ in range(E)]  # 간선의 양 끝, 가중치를 담은 리스트
    edge.sort(key=lambda x: x[2])  # 가중치를 기준으로 정렬
    parent = [i for i in range(V + 1)]  # 해당 노드의 부모를 담을 리스트
    cnt = 0  # 현재 간선의 수 MST 의 간선의 수는 V + 1
    answer = 0  # 선택된 MST 의 가중치의 합
    for v1, v2, w in edge:
        if find_set(v1) != find_set(v2):  # 대표자가 다르면 사이클 X
            union_set(v1, v2)
            cnt += 1
            answer += w
            if cnt == V + 1:  # MST 구성 끝
                break
    print(f"#{tc} {answer}")
