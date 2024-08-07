import sys

sys.stdin = open('txt/input_ws1.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 노드의 수 V, 간선의 수 E
    arr = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())  # 출발 노드, 도착 노드
    # 인접 리스트 작성
    adj_l = [[] for _ in range(V + 1)]
    for v1, v2 in arr:
        adj_l[v1].append(v2)
    # 방문 학인, 스택, 현재 위치
    visited = [0] * (V + 1)
    stack = []
    v = start  # 현재 위치를 시작점으로 초기화
    visited[start] = 1
    answer = 0
    while True:
        if v == end:  # 현재 위치가 도착점이라면 종료
            answer = 1
            break
        for w in adj_l[v]:
            if not visited[w]:
                stack.append(v)  # 위치 저장
                v = w  # 현재 위치 변경
                visited[w] = 1  # 방문 표시
                break
        else:  # for 문이 break 하지 않았다면
            if stack:  # 이전에 방문한 위치가 남아있다면
                v = stack.pop()
            else:
                break
    print(f'#{tc} {answer}')
