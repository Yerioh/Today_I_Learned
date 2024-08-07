import sys

sys.stdin = open('txt/input_hw1.txt', 'r')

for _ in range(10):
    tc, E = map(int, input().split())  # 테스트 케이스 번호, 길의 개수
    arr = list(map(int, input().split()))
    # 인접리스트로 변형
    adj_l = [[] for _ in range(100)]
    for i in range(E):
        idx, item = arr[i * 2], arr[i * 2 + 1]
        adj_l[idx].append(item)
    # 방문 표시, 스택, 현재 위치
    visited = [0] * 100
    stack = []
    v = 0  # 시작점
    visited[0] = 1
    answer = 0  # 정답 초기화
    while True:
        if v == 99:
            answer = 1
        for w in adj_l[v]:
            if not visited[w]:
                stack.append(v)  # 현재 위치 저장
                v = w  # 위치 이동
                visited[w] = 1  # 방문 표시
                break
        else:  # 반복이 break 되지 않았다면
            if stack:  # 이전에 방문한 곳이 있다면
                v = stack.pop()
            else:
                break
    print(f'#{tc} {answer}')
