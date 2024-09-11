# 위상 정렬
# BFS, DFS 모두 가능

# DFS
# 하나의 선형 순서가 결과로 나온다.
# 간선의 방향성을 유지하면서 그래프의 모든 정점을 나열
# N개의 정점
# [v1, v2, v3, ..., vn]
# 어떤 간선을 (vi, vj) 이렇게 나타냈을 때, i < j

# 비순환 그래프에서만 가능
# 결과가 유일하지 않을 수 있다.

# 깊이 우선 탐색 기반의 위상 정렬
# DFS 를 수행하면서 각 노드가 처리 되는 순서를 스택에 저장

# 모든노드를 방문한 다음에 스택의 내용을 역순으로 정렬하면서 결과 도출

# 1. 방문하지 않은 모든 정점에 대해서 DFS 실행
# 2. 어떤 정점에 대해서 그 정점과 인접한 모든 정점을 방문한 후에 스택에 추가
#    => 현재 정점에서 갈 수 있는 모든 정점을 다 탐색하고 난 뒤에 현재 정점을 스택에 추가
# 3. 스택을 역순으로 정렬하면 위상정렬이 된다.


def topology_sort(v):  # 현재 정점
    visited[v] = 1
    for item in G[v]:
        if not visited[item]:
            topology_sort(item)
    stack.append(v)


# 작업 순서
for tc in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[] for _ in range(V + 1)]
    stack = []
    visited = [0] * (V + 1)
    for i in range(E):
        s, e = arr[i * 2], arr[i * 2 + 1]
        G[s].append(e)
    for i in range(1, V + 1):
        if not visited[i]:
            topology_sort(i)
    print(f"#{tc}", *stack[::-1])

# adj_l = [[2], [2, 3], [4], [5], [5], []]  # A B C D E F
# stack = []
# visited = [0] * 6
# for i in range(6):
#     if not visited[i]:
#         topology_sort(i)
# print(stack[::-1])
