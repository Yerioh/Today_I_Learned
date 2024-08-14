"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""


# 너비 우선 탐색 함수
def bfs_(G, v):
    visited = [0] * len(G)  # 인큐 된 적 있는 지 확인
    q = [0] * (len(G) - 1)  # 원형 큐
    front = rear = 0
    answer = [0] * (len(G) - 1)  # 정답 배열
    idx = 0  # 정답 배열의 인덱스
    # enQueue
    q[rear] = v
    rear = (rear + 1) % (len(G) - 1)
    visited[v] = 1
    while idx < len(G) - 1:
        # deQueue
        t = q[front]
        front = (front + 1) % (len(G) - 1)
        answer[idx] = t
        idx += 1
        for node in G[t]:
            if not visited[node]:
                q[rear] = node
                rear = (rear + 1) % (len(G) - 1)
                visited[node] = visited[t] + 1
    print("방문 확인 :",visited)
    return answer


# 입력 받기
V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 리스트 -> 인접 리스트
adj_l = [[] for _ in range(V + 1)]
for i in range(0, E * 2, 2):
    adj_l[arr[i]].append(arr[i + 1])
    adj_l[arr[i + 1]].append(arr[i])
# 출력
print("인접 리스트 :", adj_l)
print("너비 우선 탐색 진행 순서 :", end=" ")
print(*bfs_(adj_l, 1), sep="-")
