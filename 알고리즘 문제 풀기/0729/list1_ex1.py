# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    max_v = A[0]
    min_v = A[0]
    for i in A:
        if i > max_v:
            max_v = i
        if i < min_v:
            min_v = i
    print(f'#{t} {max_v - min_v}')
