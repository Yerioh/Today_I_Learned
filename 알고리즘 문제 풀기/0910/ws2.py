"""
3
2 7
3 15
36 1007

"""
from collections import deque

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 정수 N, M
    result = 0
    q = deque()
    v = [0] * 1000001
    q.append(N)
    v[N] = 1
    while q:  # 앞의 연산 결과들을 한번씩 연산하여 넣어주기
        n = q.popleft()
        if n == M:
            result = v[n] - 1
            break
        # 연산 결과를 담은 리스트
        operation = [n + 1, n - 1, n * 2, n - 10]
        for res in operation:
            if 0 < res < 1000001 and not v[res]:
                q.append(res)
                v[res] = v[n] + 1
    print(f"#{tc} {result}")
