"""
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

# 그래프를 빠짐없이 한번씩 모두 방문하는게 목표
# 그 방법 중 하나 dfs


def dfs_(s, V):  # s: 시작 정점, V: 정점개수(1번부터인 정점의 마지막정점)
    visited = [0] * (V + 1)  # 방문한 정점을 표시
    stack = []  # 스택 생성
    print(s, end=" ")
    visited[s] = 1  # 시작 정점 방문 표시
    v = s  # 현재 정점
    while True:
        # v의 인접하고, 방문안한  w가 있으면
        for w in adjL[v]:
            if not visited[w]:
                stack.append(v)  # 현재 정점을 push
                v = w  # w에 방문
                print(v, end=" ")
                visited[w] = 1  # w에 방문 표시
                break
        else:
            if stack:  # 이전 갈림길으로 돌아가기
                v = stack.pop()
            else:  # 되돌아갈 곳이 없거나 남은 갈림길이 없으면 탐색종료
                break
    print()


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    # 인접 리스트로 저장
    adjL = [[] for _ in range(V + 1)]
    arr = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    print(adjL)  # [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
    dfs_(1, V)

    # 인접 행렬로 저장
    adj_m = [[0] * V for _ in range(V)]
    for i in range(E):
        r, c = arr[i * 2] - 1, arr[i * 2 + 1] - 1
        adj_m[r][c] = 1
        adj_m[c][r] = 1
    print(adj_m)
    #   1  2  3  4  5  6  7
    # [[0, 1, 1, 0, 0, 0, 0], 1
    #  [1, 0, 0, 1, 1, 0, 0], 2
    #  [1, 0, 0, 0, 0, 0, 1], 3
    #  [0, 1, 0, 0, 0, 1, 0], 4
    #  [0, 1, 0, 0, 0, 1, 0], 5
    #  [0, 0, 0, 1, 1, 0, 1], 6
    #  [0, 0, 1, 0, 0, 1, 0]] 7
