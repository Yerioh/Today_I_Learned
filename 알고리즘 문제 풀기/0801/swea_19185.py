T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr_s = input().split()  # N개의 문자열
    arr_t = input().split()  # M개의 문자열
    Q = int(input())
    arr_q = [int(input()) for _ in range(Q)]  # Q개의 연도
    answer = [''] * Q  # Q개의 정답
    for i in range(Q):
        si = (arr_q[i] - 1) % N
        ti = (arr_q[i] - 1) % M
        answer[i] = arr_s[si] + arr_t[ti]
    print(f'#{tc}', end=' ')
    print(*answer)
